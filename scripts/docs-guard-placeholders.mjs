import { read, walk } from './docs-utils.mjs';

const strict = process.env.STRICT_PLACEHOLDERS === '1';
const files = walk('docs', f => f.endsWith('.md'));
const pattern = /<[A-Z0-9_]+>/g;
let count = 0;

for (const file of files) {
  const content = read(file);
  const matches = [...content.matchAll(pattern)].map(m => m[0]);
  if (matches.length) {
    count += matches.length;
    const sample = [...new Set(matches)].slice(0, 6).join(', ');
    const msg = `PLACEHOLDER ${strict ? 'FAIL' : 'WARN'} ${file}: ${sample}`;
    if (strict) console.error(msg); else console.warn(msg);
  }
}

if (!count) console.log('placeholders ok');
else if (!strict) console.log(`placeholder scan completed with ${count} template placeholder(s); set STRICT_PLACEHOLDERS=1 to fail.`);
process.exit(strict && count ? 1 : 0);
