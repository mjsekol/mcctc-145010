# Template · Licensing Statement
## 145010 Senior Capstone · started Week 8, current every week

**Commit as:** `LICENSING.md` at the top of your repository.
**Due:** started Week 8 with the ownership decision. Updated every time you add a library, asset,
font, icon, model, or dataset. Complete for the release candidate in Week 14.

**Competencies this evidences:** 1.3.8 (verify compliance with computer and intellectual property
laws and regulations), 1.7.13 (protect intellectual property and knowledge), 1.2.1 (extract valid
information and cite sources).

---

## Why this exists

**Your project is a stack of work owned by different people.** Your code, a framework, a dozen
libraries, an icon set, a font, maybe a model, and your stakeholder's documents. Each one came with
permission, and most permissions come with conditions. This file shows you met them.

**It also answers a question your stakeholder will eventually ask:** "Are we allowed to keep using
this after you leave?"

**The failure to avoid is reading a summary instead of the license.** A badge on a repository page
or an answer from a chat tool is not the license. Open the license file that shipped with the thing
you used. You practiced this in 145130.

**This is not legal advice.** It is a careful record by someone who is not a lawyer. Say so at the
top of your file.

---

## The four questions, for every license

1. **What does it permit?**
2. **What does it require** in exchange: a notice kept, a copy of the license shipped, changes
   marked, credit given in a particular form, the same license passed on?
3. **What does it forbid?**
4. **What triggers the requirements?** Many conditions apply when you distribute or convey the
   work, not when you use it privately. Handing your stakeholder a copy is distributing. Check
   yours.

---

```markdown
# Licensing Statement · <project name>
Last updated: Week <n>, <day>

*This is a record of the licenses in this project, written by a student who is not a lawyer. It is
not legal advice.*

## 1. This project's own code
- **Copyright holder:** <you, as agreed in the acceptance agreement>
- **License this project is released under:** <name, and the LICENSE file in this repository>
- **What the stakeholder may do:** <in plain words, matching the agreement>

## 2. Libraries and frameworks
*Every dependency your project installs directly. Check your requirements file, project file, or
package list, not your memory.*

| Name | Version | License | Permits | Requires | Forbids | How I met the requirements |
|---|---|---|---|---|---|---|
| | | | | | | <notice kept in ..., license copied to ...> |

**How I produced this list:** <the command or file you read>

## 3. Images, icons, fonts, audio, and video
| Asset | Where it is used | Source | License | Attribution required? | Where the attribution appears |
|---|---|---|---|---|---|
| | | | | | |

*An image found by a search is not licensed for your use because it was findable. If you cannot
name the license, do not use it.*

## 4. Models
*AI-Integrated track, and anyone whose project calls a model.*

| Model | Version | Downloaded from | License file | Approved by instructor |
|---|---|---|---|---|
| | | | | Week <n>, <day> |

**Use restrictions, quoted from the license:**
> <quote>

**Why this project's use is permitted:** <with the clause>
**What I could not determine:** <and who could answer it>

## 5. The stakeholder's materials
| Material | Permission given | Where it is recorded | Conditions |
|---|---|---|---|
| <their logo, documents, manuals, data> | <yes, in writing> | <meeting record or email, week and day> | <internal use only, etc.> |

## 6. AI-assisted work
- **Where AI tools contributed:** see `ai-usage-log.md`.
- **What is honestly uncertain:** <ownership of generated output is an open question in places.
  State what you know and what you do not.>

## 7. Data
- **Data this project stores or reads, and who owns it:** <...>
- **Personal data:** <none / only what the data dictionary lists>

## 8. How I checked
- <the command, file, or page for each section, and the week and day>
```

---

## Before you commit · self-check

- [ ] Every row in section 2 comes from your actual dependency file.
- [ ] Every license was read from the license text, not a summary.
- [ ] Every attribution a license requires actually appears where section 3 says it does.
- [ ] Section 5 has written permission for every stakeholder material you use.
- [ ] The not-legal-advice line is at the top.
