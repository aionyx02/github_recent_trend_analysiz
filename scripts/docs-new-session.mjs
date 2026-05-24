import { exists, read, today, write } from './docs-utils.mjs';

const date = today();
const file = `docs/memory/sessions/${date}.md`;

if (exists(file)) {
  console.log(`${file} already exists`);
  process.exit(0);
}

const template = exists('docs/memory/sessions/YYYY-MM-DD.md')
  ? read('docs/memory/sessions/YYYY-MM-DD.md').replaceAll('YYYY-MM-DD', date)
  : `---\ntype: session_log\nstatus: archive\nupdated: ${date}\ncontext_policy: historical\nowner: project\n---\n\n# Session Log: ${date}\n`;

write(file, template);
console.log(`created ${file}`);
