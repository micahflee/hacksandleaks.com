const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

const inputDir = path.join(__dirname, '..', 'md');
const outputDir = 'output'; // the directory where your static HTML files will be generated

function generateHTML(markdown) {
  if (!markdown) {
    console.error('Error: markdown content is undefined or null');
    return '';
  }
  
  const html = marked(markdown);
  
  // Wrap Summary section in a div with a class
  const div = document.createElement('div');
  div.innerHTML = html;
  const summary = div.querySelector('#summary');
  if (summary) {
    summary.outerHTML = `<div class="summary" id="summary">${summary.innerHTML}</div>`;
  }
  
  // Apply CSS to prevent Markdown parser from interpreting Summary section contents
  const css = '<style>.summary * { display: inline; }</style>';
  return css + div.innerHTML;
}

function readTemplate() {
  return fs.readFileSync(path.join(__dirname, '..', 'template.html'), 'utf8');
}

function writeHTML(outputPath, html) {
  fs.writeFileSync(outputPath, html, 'utf8');
}

function processMarkdownFile(filePath, chapterName, fileName) {
  const markdown = fs.readFileSync(filePath, 'utf8');
  const html = generateHTML(markdown);
  const outputPath = path.join(outputDir, chapterName, `${fileName}.html`);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, html);
}

function calculateReadTime(text) {
  const wordsPerMinute = 200;
  const wordCount = text.split(/\s+/).length;
  return Math.ceil(wordCount / wordsPerMinute);
}

function build() {
  // Ensure output directory exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
  }

  const chapters = ['introduction', 'chapter-1', 'chapter-2', 'chapter-3'];

  for (const [index, chapter] of chapters.entries()) {
    const chapterPath = path.join(inputDir, chapter);

    // Read intro, body, and pagination markdown files for each chapter
    const introMd = fs.readFileSync(path.join(chapterPath, 'intro.md'), 'utf-8');
    const bodyMd = fs.readFileSync(path.join(chapterPath, 'body.md'), 'utf-8');
    const paginationMd = fs.readFileSync(path.join(chapterPath, 'pagination.md'), 'utf-8');
    
    // Calculate read time
    const readTime = calculateReadTime(introMd + bodyMd);
    
    const navHTML = marked(fs.readFileSync(path.join(inputDir, 'nav.md'), 'utf-8'));
    const introHTML = `<div id="reading-time">~${readTime} min read</div>` + marked(introMd);
    const bodyHTML = marked(bodyMd);
    const paginationHTML = marked(paginationMd);
    const footerHTML = marked(fs.readFileSync(path.join(inputDir, 'footer.md'), 'utf-8'));

    // Generate HTML and write to output file
    const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${chapter.charAt(0).toUpperCase() + chapter.slice(1)}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="wrapper">
           <h1>Hacks, Leaks, and Revelations</h1>
            <nav>
                <div id="nav">${navHTML}</div>
                <a class="mobileNav btnIcon"></a>
                <a href="https://nostarch.com/hacks-leaks-and-revelations" role="button" class="primaryBtn btn">Pre-Order</a>
            </nav>
        </div>
    </header>
    <section class="intro">
        <div class="wrapper" id="intro-wrapper">${introHTML}</div>
    </section>
    <section id="content" data-content="${chapter}">
        <div class="wrapper" id="about-content">${bodyHTML}</div>
    </section>
    <section class="pagination">
        <div class="wrapper" id="pagination-content">${paginationHTML}</div>
    </section>
    <footer id="footer">
        <div class="wrapper" id="footer-content">${footerHTML}</div>
    </footer>
    <script src="js/jquery-min.js"></script>
    <script src="js/main.js"></script>
</body>
</html>`;

    const outputFilename = index === 0 ? 'introduction.html' : `chapter-${index}.html`;
    fs.writeFileSync(path.join(outputDir, outputFilename), htmlContent);
  }
}

build();
