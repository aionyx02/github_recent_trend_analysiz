import { spawnSync } from 'node:child_process';

const steps = [
  ['docs:completed-regen', 'node', ['scripts/docs-completed-regen.mjs']],
  ['docs:sync', 'node', ['scripts/docs-sync.mjs']],
  ['docs:guard-size', 'node', ['scripts/docs-guard-size.mjs']],
  ['docs:guard-schema', 'node', ['scripts/docs-guard-schema.mjs']],
  ['docs:guard-links', 'node', ['scripts/docs-guard-links.mjs']],
  ['docs:guard-placeholders', 'node', ['scripts/docs-guard-placeholders.mjs']],
  ['docs:guard-adr-status', 'node', ['scripts/docs-guard-adr-status.mjs']],
  ['docs:guard-task-status', 'node', ['scripts/docs-guard-task-status.mjs']],
  ['docs:audit-frontmatter', 'node', ['scripts/docs-audit-frontmatter.mjs']],
  ['docs:narrative-check', 'node', ['scripts/docs-narrative-check.mjs']]
];

for (const [name, cmd, args] of steps) {
  console.log(`\n> ${name}`);
  const result = spawnSync(cmd, args, { stdio: 'inherit', shell: process.platform === 'win32' });
  if (result.status !== 0) process.exit(result.status ?? 1);
}
console.log('\ndocs refresh ok');
