## Generate static HTML from markdown

Your content publishes as static HTML, but is editable as markdown.

Make sure you have nodejs installed, and install deps:

```
apt install -y nodejs npm

cd src
npm install
```

When your markdown is ready, run:

```
node build.js
```