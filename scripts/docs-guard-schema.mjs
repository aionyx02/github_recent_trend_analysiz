import { parseFrontmatter, read, walk } from './docs-utils.mjs';

const required = ['type', 'status', 'updated', 'context_policy', 'owner'];
let failed = false;

for (const file of walk('docs', f => f.endsWith('.md'))) {
  const fm = parseFrontmatter(read(file));
  if (!fm) {
    console.error(`FRONTMATTER MISSING ${file}`);
    failed = true;
    continue;
  }
  for (const key of required) {
    if (!fm[key]) {
      console.error(`FRONTMATTER KEY MISSING ${file}: ${key}`);
      failed = true;
    }
  }
}

if (!failed) console.log('schema ok');
process.exit(failed ? 1 : 0);
