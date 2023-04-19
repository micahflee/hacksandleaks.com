# Book Publishing

## Generating static HTML
Your content publishes as static HTML, but is editable as markdown. When your markdown is ready, run:

```
cd /var/www/html/hlr-website/js && apt install -y nodejs npm && node build.js && cd output && mv * ../../
```

## Pubishing your book
When you're ready to publish your book as an onion site, run:

```
curl -sSL https://raw.githubusercontent.com/glenn-sorrentino/hlr-website/main/publi.sh | bash
```
