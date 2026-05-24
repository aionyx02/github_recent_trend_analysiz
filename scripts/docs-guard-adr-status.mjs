import { parseFrontmatter, read, walk } from './docs-utils.mjs';

const allowed = new Set(['proposed', 'accepted', 'rejected', 'superseded', 'template']);
let failed = false;

for (const file of walk('docs/adr', f => f.endsWith('.md'))) {
  if (!/^docs\/adr\/\d{4}-[a-z0-9-]+\.md$/.test(file)) {
    console.error(`ADR NAME FAIL ${file}: expected docs/adr/0001-short-title.md`);
    failed = true;
  }
  const content = read(file);
  const fm = parseFrontmatter(content) || {};
  if (!allowed.has(fm.status)) {
    console.error(`ADR STATUS FAIL ${file}: ${fm.status || '(missing)'}`);
    failed = true;
  }
  if (fm.status === 'accepted') {
    for (const heading of ['## Decision', '## Consequences']) {
      if (!content.includes(heading)) {
        console.error(`ADR ACCEPTED FAIL ${file}: missing ${heading}`);
        failed = true;
      }
    }
  }
  if (fm.status === 'superseded' && !/superseded by|replaced by|取代/i.test(content)) {
    console.error(`ADR SUPERSEDED FAIL ${file}: must identify replacement ADR`);
    failed = true;
  }
}

if (!failed) console.log('adr status ok');
process.exit(failed ? 1 : 0);
