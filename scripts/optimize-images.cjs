const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');

(async () => {
  const source = 'public/assets';
  const output = path.join(source, 'optimized');
  fs.mkdirSync(output, { recursive: true });
  const manifest = {};
  for (const file of fs.readdirSync(source).filter(name => /\.jpg$/i.test(name))) {
    const input = path.join(source, file);
    const metadata = await sharp(input).metadata();
    const widths = [...new Set([320, 640, 960, 1440].map(width => Math.min(width, metadata.width)))];
    const variants = [];
    for (const width of widths) {
      const name = `${path.parse(file).name}-${width}.webp`;
      const target = path.join(output, name);
      if (!fs.existsSync(target) || fs.statSync(target).mtimeMs < fs.statSync(input).mtimeMs) {
        await sharp(input).resize({ width, withoutEnlargement: true }).webp({ quality: 78, effort: 5 }).toFile(target);
      }
      const info = await sharp(target).metadata();
      variants.push({ src: `/assets/optimized/${name}`, width: info.width, height: info.height, bytes: fs.statSync(target).size });
    }
    manifest[file] = { width: metadata.width, height: metadata.height, originalBytes: fs.statSync(input).size, variants };
  }
  fs.writeFileSync('src/data/images.json', JSON.stringify(manifest, null, 2) + '\n');
  console.log(`WebP responsivo: ${Object.keys(manifest).length} fotos, sem ampliar os originais.`);
})().catch(error => { console.error(error); process.exitCode = 1; });
