#!/usr/bin/env node
/*
 * web-check: validate HTML and audit accessibility the way the 145010 course requires.
 *
 *   node tools/web-check/check.js <page.html> [more.html ...] [options]
 *
 *   --widths 360,768,1280   viewport widths to test (default 360,768,1280)
 *   --shots <folder>        save a full-page screenshot at each width
 *   --no-validate           skip HTML validation
 *   --no-axe                skip the accessibility audit
 *   --json                  print one JSON object per page instead of text
 *
 * What it checks, per page:
 *   1. HTML validation with html-validate (recommended rules). Offline, no network.
 *   2. An automated accessibility audit with axe-core, run inside headless Chrome at
 *      every width, WCAG 2.x A and AA rules.
 *   3. Horizontal overflow at every width: the page is wider than the viewport, which is
 *      the usual sign that a layout is not responsive.
 *
 * Exit code 0 only when every page has zero validation errors, zero axe violations, and
 * no horizontal overflow at any width. Automated tools catch only part of what matters:
 * keyboard order, meaningful alt text, and screen reader experience still need a human.
 */
"use strict";

const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");

const CHROME_CANDIDATES = [
  process.env.CHROME_PATH,
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "/usr/bin/google-chrome",
  "/usr/bin/chromium",
].filter(Boolean);

function parseArgs(argv) {
  const opts = { pages: [], widths: [360, 768, 1280], shots: null, validate: true, axe: true, json: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--widths") opts.widths = argv[++i].split(",").map((n) => parseInt(n, 10));
    else if (a === "--shots") opts.shots = argv[++i];
    else if (a === "--no-validate") opts.validate = false;
    else if (a === "--no-axe") opts.axe = false;
    else if (a === "--json") opts.json = true;
    else opts.pages.push(a);
  }
  return opts;
}

async function validate(file) {
  const { HtmlValidate, FileSystemConfigLoader } = require("html-validate");
  // The recommended preset, minus two rules that are style opinions rather than validity:
  // a lowercase <!doctype html> is valid HTML5, and 145010 Week 2 teaches inline styles
  // as a competency (6.1.7), so flagging every inline style would fail correct lessons.
  const loader = new FileSystemConfigLoader({
    extends: ["html-validate:recommended"],
    rules: { "doctype-style": "off", "no-inline-style": "off" },
  });
  const validator = new HtmlValidate(loader);
  const report = await validator.validateFile(file);
  const messages = [];
  for (const result of report.results) {
    for (const m of result.messages) {
      messages.push({ line: m.line, column: m.column, rule: m.ruleId, message: m.message, severity: m.severity });
    }
  }
  return { errors: messages.filter((m) => m.severity === 2), warnings: messages.filter((m) => m.severity === 1) };
}

async function audit(browser, file, widths, shotsDir) {
  const axeSource = fs.readFileSync(require.resolve("axe-core/axe.min.js"), "utf8");
  const page = await browser.newPage();
  const byWidth = [];
  try {
    for (const width of widths) {
      await page.setViewport({ width, height: 900 });
      await page.goto(pathToFileURL(path.resolve(file)).href, { waitUntil: "load" });
      await page.addScriptTag({ content: axeSource });
      const result = await page.evaluate(async () => {
        // eslint-disable-next-line no-undef
        const r = await axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"] } });
        return r.violations.map((v) => ({
          id: v.id,
          impact: v.impact,
          help: v.help,
          nodes: v.nodes.length,
          targets: v.nodes.slice(0, 3).map((n) => n.target.join(" ")),
        }));
      });
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      if (shotsDir) {
        fs.mkdirSync(shotsDir, { recursive: true });
        const base = path.basename(file, path.extname(file));
        await page.screenshot({ path: path.join(shotsDir, `${base}-${width}.png`), fullPage: true });
      }
      byWidth.push({ width, violations: result, overflowPx: Math.max(0, overflow) });
    }
  } finally {
    await page.close();
  }
  return byWidth;
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.pages.length === 0) {
    console.error("usage: node tools/web-check/check.js <page.html> [more.html ...] [--widths 360,768,1280] [--shots dir]");
    process.exit(2);
  }
  let browser = null;
  if (opts.axe) {
    const chrome = CHROME_CANDIDATES.find((p) => fs.existsSync(p));
    if (!chrome) {
      console.error("No Chrome or Edge found. Set CHROME_PATH, or pass --no-axe.");
      process.exit(2);
    }
    const puppeteer = require("puppeteer-core");
    browser = await puppeteer.launch({ executablePath: chrome, headless: true, args: ["--allow-file-access-from-files"] });
  }
  let failed = false;
  try {
    for (const file of opts.pages) {
      if (!fs.existsSync(file)) {
        console.error(`MISSING  ${file}`);
        failed = true;
        continue;
      }
      const out = { page: file, validation: null, widths: null };
      if (opts.validate) out.validation = await validate(file);
      if (opts.axe) out.widths = await audit(browser, file, opts.widths, opts.shots);

      const vErrors = out.validation ? out.validation.errors.length : 0;
      const axeCount = out.widths ? out.widths.reduce((n, w) => n + w.violations.length, 0) : 0;
      const overflowAt = out.widths ? out.widths.filter((w) => w.overflowPx > 0).map((w) => w.width) : [];
      const ok = vErrors === 0 && axeCount === 0 && overflowAt.length === 0;
      if (!ok) failed = true;

      if (opts.json) {
        console.log(JSON.stringify({ ...out, ok }));
        continue;
      }
      console.log(`${ok ? "PASS" : "FAIL"}  ${file}`);
      if (out.validation) {
        console.log(`  validation: ${vErrors} error(s), ${out.validation.warnings.length} warning(s)`);
        for (const m of out.validation.errors) console.log(`    line ${m.line}:${m.column}  ${m.rule}  ${m.message}`);
      }
      if (out.widths) {
        for (const w of out.widths) {
          const extra = w.overflowPx > 0 ? `, OVERFLOWS by ${w.overflowPx}px` : "";
          console.log(`  axe at ${w.width}px: ${w.violations.length} violation(s)${extra}`);
          for (const v of w.violations) console.log(`    ${v.id} (${v.impact}, ${v.nodes} node(s))  ${v.help}  e.g. ${v.targets.join(" | ")}`);
        }
      }
    }
  } finally {
    if (browser) await browser.close();
  }
  process.exit(failed ? 1 : 0);
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});
