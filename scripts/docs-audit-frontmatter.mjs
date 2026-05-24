import { parseFrontmatter, read, walk } from './docs-utils.mjs';

let failed = false;
const validContext = new Set(['always_retrievable', 'on_demand', 'retrieve_only', 'retrieve_when_planning', 'retrieve_when_debugging', 'historical']);

for (const file of walk('docs', f => f.endsWith('.md'))) {
  const fm = parseFrontmatter(read(file));
  if (!fm) continue;
  if (fm.context_policy && !validContext.has(fm.context_policy)) {
    console.error(`UNKNOWN context_policy ${file}: ${fm.context_policy}`);
    failed = true;
  }
}

if (!failed) console.log('frontmatter audit ok');
process.exit(failed ? 1 : 0);
