import fs from 'node:fs';
import { ROOT } from './docs-utils.mjs';
import path from 'node:path';

const limits = [
  ['docs/memory/current.md', 5 * 1024],
  ['docs/tasks/active.md', 5 * 1024],
  ['docs/state/tasks-summary.json', 6 * 1024],
  ['docs/state/decision-summary.json', 3 * 1024],
  ['docs/ui.md', 6 * 1024],
  ['docs/html-guidelines.md', 6 * 1024],
  ['docs/design-system.md', 6 * 1024],
  ['docs/accessibility.md', 6 * 1024],
  ['docs/conventions.md', 6 * 1024],
  ['docs/dependencies.md', 6 * 1024],
  ['docs/data.md', 6 * 1024]
];

let failed = false;
for (const [file, limit] of limits) {
  const full = path.join(ROOT, file);
  if (!fs.existsSync(full)) continue;
  const size = fs.statSync(full).size;
  if (size > limit) {
    console.error(`SIZE FAIL ${file}: ${size} > ${limit}`);
    failed = true;
  } else {
    console.log(`SIZE OK ${file}: ${size}/${limit}`);
  }
}
process.exit(failed ? 1 : 0);
