Here's how to convert the book to Markdown.

- Run `make_markdown.sh` to use pandoc to convert the EPUB file to `book.md`.
- Run `build.py` to load `book.md` and make `book_simplified.md`, then copy and paste from that into the chapters.
- For each chapter, search for these strings to manually fix issues: `Figure`, `["`, `Xref`, `aria-label`, `Index-Link`, `LinkTwitter`, `<aside class="box"`, `https://`, `.small`, `note_`, `.sample`, `.xhtml`, "```", "` `"
