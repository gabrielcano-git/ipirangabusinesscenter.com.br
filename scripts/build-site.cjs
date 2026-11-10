const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'ibc-build-'));
function run(file, args = []) {
  const result = spawnSync(process.execPath, [file, ...args], { stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) throw new Error(`${file}: exit ${result.status}`);
}
try {
  run('scripts/optimize-images.cjs');
  run('scripts/build.cjs');
  run('scripts/build-reports.cjs');
  const css = path.join(temporary, 'site.css');
  run('node_modules/sass/sass.js', ['src/styles/site.scss', css, '--no-source-map']);
  run('node_modules/tailwindcss/lib/cli.js', ['-c', 'tailwind.config.cjs', '-i', css, '-o', 'dist/assets/site.css', '--minify']);
  run('scripts/inline-css.cjs');
} finally {
  fs.rmSync(temporary, { recursive: true, force: true });
}
