import { read, walk } from './docs-utils.mjs';

const active = read('docs/tasks/active.md');
const ids = [...active.matchAll(/\bTASK\.[A-Z0-9.]+\b/g)].map(m => m[0]);
let failed = false;
const seen = new Set();
for (const id of ids) {
  if (seen.has(id)) {
    console.error(`TASK ID FAIL docs/tasks/active.md: duplicate ${id}`);
    failed = true;
  }
  seen.add(id);
}

for (const m of active.matchAll(/- Status:\s*([^\n]+)/g)) {
  const status = m[1].trim();
  if (!['todo', 'doing', 'blocked', 'review', 'done'].includes(status)) {
    console.error(`TASK STATUS FAIL docs/tasks/active.md: ${status}`);
    failed = true;
  }
}

for (const file of walk('docs/memory/sessions', f => f.endsWith('.md') && !f.endsWith('YYYY-MM-DD.md'))) {
  const content = read(file);
  for (const line of content.split('\n')) {
    if (line.startsWith('## COMPLETED:') && !/^## COMPLETED:\s*TASK\.[A-Z0-9.]+\s+-\s+.+/.test(line)) {
      console.error(`COMPLETED MARKER FAIL ${file}: ${line}`);
      failed = true;
    }
  }
}

if (!failed) console.log('task status ok');
process.exit(failed ? 1 : 0);
