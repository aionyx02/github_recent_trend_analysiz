import fs from 'node:fs';

const dirs = [
  'docs/adr',
  'docs/memory/sessions',
  'docs/memory/archive',
  'docs/tasks',
  'docs/state',
  'scripts'
];
for (const dir of dirs) fs.mkdirSync(dir, { recursive: true });
console.log('context directories ready');
