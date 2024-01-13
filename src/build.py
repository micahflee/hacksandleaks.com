#!/usr/bin/env python3

import os
import markdown
from bs4 import BeautifulSoup

input_dir = "md"
output_dir = ".."


def generate_html(markdown_content):
    if not markdown_content:
        print("Error: markdown content is undefined or null")
        return ""

    html = markdown.markdown(markdown_content)

    # Wrap Summary section in a div with a class
    soup = BeautifulSoup(html, "html.parser")
    summary = soup.find(id="summary")
    if summary:
        summary.wrap(soup.new_tag("div", **{"class": "summary"}))

    # Apply CSS to prevent Markdown parser from interpreting Summary section contents
    css = "<style>.summary * { display: inline; }</style>"
    return css + str(soup)


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def calculate_read_time(text):
    words_per_minute = 200
    word_count = len(text.split())
    return round(word_count / words_per_minute)


def build():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Make a list of folder names in the md folder
    chapters = []
    for _, dirs, _ in os.walk(input_dir):
        for name in dirs:
            chapters.append(name)

    for chapter in chapters:
        chapter_path = os.path.join(input_dir, chapter)
        title = read_file(os.path.join(chapter_path, "title.txt"))

        intro_md = read_file(os.path.join(chapter_path, "intro.md"))
        body_md = read_file(os.path.join(chapter_path, "body.md"))
        pagination_md = read_file(os.path.join(chapter_path, "pagination.md"))

        read_time = calculate_read_time(intro_md + body_md)

        nav_html = markdown.markdown(read_file(os.path.join(input_dir, "nav.md")))
        intro_html = markdown.markdown(intro_md)
        body_html = markdown.markdown(body_md)
        pagination_html = markdown.markdown(pagination_md)
        footer_html = markdown.markdown(read_file(os.path.join(input_dir, "footer.md")))

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="author" content="Micah Lee">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Buy Hacks, Leaks, and Revelations: The Art of Analyzing Hacked and Leaked Data by Micah Lee.">
    <meta name="apple-mobile-web-app-title" content="Hacks, Leaks, and Revelations">
    <meta name="application-name" content="Hacks, Leaks, and Revelations">
    <meta name="theme-color" content="#86D58D">

    <title>{title} - Hacks, Leaks, and Revelations</title>

    <link rel="apple-touch-icon" sizes="180x180" href="images/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" href="images/favicon/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="images/favicon/favicon-16x16.png" sizes="16x16">
    <link rel="icon" type="image/png" href="images/favicon/android-chrome-192x192.png" sizes="192x192">
    <link rel="icon" type="image/png" href="images/favicon/android-chrome-512x512.png" sizes="512x512">
    <link rel="icon" type="image/x-icon" href="images/favicon/favicon.ico">

    <link rel="stylesheet" href="css/style.css">
    <script defer data-domain="hacksandleaks.com" data-api="https://deniability.brisk.workers.dev/deniability/event" src="https://deniability.brisk.workers.dev/deniability/script.js"></script>
</head>
<body>
    <header>
        <div class="wrapper">
           <h1><a href="/">Hacks, Leaks, and Revelations</a></h1>
            <nav>
                <div id="nav">{nav_html}</div>
                <a class="mobileNav btnIcon"></a>
                <a href="buy.html" role="button" class="primaryBtn btn">Buy Now</a>
            </nav>
        </div>
    </header>
    <section class="intro bookIntro">
        <div class="wrapper" id="intro-wrapper">
          <div id="reading-time">~{read_time} min read</div>
          <h1>{title}</h1>
          {intro_html}
        </div>
    </section>
    <section id="content" data-content="{chapter}">
        <div class="wrapper" id="about-content">{body_html}
        </div>
    </section>
    <section class="buy">
        <div class="wrapper">
            <h3>Information Wants to be Free</h3>
            <p><strong>Everyone should have access to the information in this book.</strong> To remove barriers to access, I've made Hacks, Leaks, and Revelations available for free online under a <a href="license.html">Creative Commons license</a>. If you can afford it, show your support and <a href="buy.html">buy a copy</a> today! (The physical book is also much nicer to read.)</p>
        </div>
    </section>
    <section class="pagination">
        <div class="wrapper" id="pagination-content">{pagination_html}</div>
    </section>
    <footer id="footer">
        <div class="wrapper" id="footer-content">{footer_html}</div>
    </footer>
</body>
</html>"""

        output_filename = f"{chapter}.html"
        write_file(os.path.join(output_dir, output_filename), html_content)


build()
