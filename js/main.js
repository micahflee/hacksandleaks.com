async function loadMarkdown(containerId, filePath, isIntro) {
  const response = await fetch(filePath);
  const markdown = await response.text();
  const container = document.getElementById(containerId);

  // Add content
  const contentElement = document.createElement("div");
  contentElement.innerHTML = marked(markdown);
  container.appendChild(contentElement);

  if (isIntro) {
    // Calculate reading time
    const words = markdown.split(/\s+/g).length;
    const readingTime = Math.ceil(words / 200); // Assuming 200 words per minute

    // Add reading time element
    const readingTimeElement = document.createElement("div");
    readingTimeElement.id = "reading-time";
    readingTimeElement.innerHTML = `${readingTime} min read`;
    container.insertBefore(readingTimeElement, container.firstChild);
  }
}

window.addEventListener("DOMContentLoaded", async () => {
  await loadMarkdown("nav", "md/nav.md");
  await loadMarkdown("footer-content", "md/footer.md");

  const contentId = document.getElementById("content").dataset.content;
  if (contentId) {
    await loadMarkdown("intro-wrapper", `md/${contentId}/intro.md`, true);
    await loadMarkdown("about-content", `md/${contentId}/body.md`, false);
    await loadMarkdown("pagination-content", `md/${contentId}/pagination.md`, false);
    countWords();
  }
});

function countWords() {
  const body = document.getElementById('about-content');
  const words = body.innerText.trim().split(/\s+/).length;
  const readingTime = Math.ceil(words / 200); // assuming an average reading speed of 200 words per minute
  const readingTimeText = readingTime === 1 ? '1 minute' : `~${readingTime} min read`;
  const readingTimeElement = document.getElementById('reading-time');
  readingTimeElement.innerText = readingTimeText;
}

$(document).ready(function() {
  $('.btnIcon').on('click', function() {
    $('nav ul').toggleClass('show');
  });

  $('nav li').on('click', function() {
    $('header nav ul').removeClass('show');
  });
});


