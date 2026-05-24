import path from 'node:path';
import { exists, read, walk } from './docs-utils.mjs';

const markdownFiles = walk('docs', f => f.endsWith('.md')).concat(['README.md', 'CLAUDE.md'].filter(exists));
const linkPatterns = [
  /`((?:docs|scripts)\/[^`\n]+?)`/g,
  /\]\(((?:docs|scripts)\/[^)\n#]+)(?:#[^)\n]+)?\)/g
];

const ignored = new Set([
  'docs/adr/*',
  'docs/memory/sessions/*',
  'docs/memory/archive/*',
  'docs/tasks/*.md'
]);

let failed = false;
for (const file of markdownFiles) {
  const content = read(file).replace(/```[\s\S]*?```/g, '');
  for (const pattern of linkPatterns) {
    for (const m of content.matchAll(pattern)) {
      const target = m[1].trim().replace(/,$/, '');
      if ([...ignored].some(i => target.includes('*') || i === target)) continue;
      if (target.endsWith('/*')) continue;
      if (!target.match(/\.(md|mjs|json|yml|yaml)$/)) continue;
      const normalized = target.split('#')[0];
      if (!exists(normalized)) {
        console.error(`LINK FAIL ${file}: ${normalized} does not exist`);
        failed = true;
      }
    }
  }
}

if (!failed) console.log('links ok');
process.exit(failed ? 1 : 0);
