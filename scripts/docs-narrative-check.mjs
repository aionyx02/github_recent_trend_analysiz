import { read } from './docs-utils.mjs';

const checked = ['docs/memory/current.md', 'docs/tasks/active.md'];
const banned = [
  /Recent Execution Notes/i,
  /Last Confirmed Progress/i,
  /Session History/i,
  /Detailed Notes/i,
  /Bugfix Round/i,
  /^##\s*20\d{2}-\d{2}-\d{2}/m,
  /```(?:bash|sh|zsh|powershell|text)?\n[\s\S]{800,}?```/m
];

let failed = false;
for (const file of checked) {
  let content = '';
  try { content = read(file); } catch { continue; }
  for (const pattern of banned) {
    if (pattern.test(content)) {
      console.error(`NARRATIVE ROUTING FAIL ${file}: ${pattern}`);
      failed = true;
    }
  }
}

if (!failed) console.log('narrative routing ok');
process.exit(failed ? 1 : 0);
