// Ridgeview Robotics Club: parts checkout data.
//
// Ridgeview Robotics Club is an invented organization, a composite of high
// school robotics clubs. No real club is involved, and every name and note
// here is invented.
//
// TODAY is a fixed reference date so the "due back within 7 days" count is the
// same every time the page loads, on any machine, in any year. It is invented
// sample data, not a real calendar date. Change it to move the reference point.
const TODAY = "2026-03-02";

// Each checkout: the part, who has it, a short note, when it went out, and when
// it is due back. Dates are invented.
const CHECKOUTS = [
  { part: "Arduino Uno",          member: "Jalen",   note: "For the line-follower demo",   checkedOut: "2026-02-24", dueBack: "2026-03-05" },
  { part: "Soldering iron",       member: "Priya",   note: "Tip needs replacing after",    checkedOut: "2026-02-20", dueBack: "2026-03-09" },
  { part: "PLA filament, blue",   member: "Marcus",  note: "For the chassis print",        checkedOut: "2026-03-01", dueBack: "2026-03-16" },
  { part: "Servo motors, set of 4", member: "Aubrey", note: "Competition arm build",       checkedOut: "2026-02-25", dueBack: "2026-03-04" },
  { part: "Multimeter",           member: "Deshawn", note: "Debugging the power board",    checkedOut: "2026-02-28", dueBack: "2026-03-20" },
  { part: "Raspberry Pi 4",       member: "Hana",    note: "Vision experiments",           checkedOut: "2026-03-02", dueBack: "2026-03-06" },
];
