function generateRandomString(length) {
  const charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let result = "";
  for (let i = 0; i < length; i++) {
    result += charset.charAt(Math.floor(Math.random() * charset.length));
  }
  return result;
}

function cipherAnimation(element, duration) {
  const originalText = element.textContent;
  element.textContent = btoa(originalText);

  let decipherProgress = 0;
  const decipherInterval = setInterval(function () {
    const newText = originalText.slice(0, decipherProgress) + btoa(originalText.slice(decipherProgress));
    element.textContent = newText;
    decipherProgress++;

    if (decipherProgress > originalText.length) {
      clearInterval(decipherInterval);
    }
  }, duration / originalText.length);
}

const title = document.querySelector(".cipher-title");
cipherAnimation(title, 2000); // You can adjust the duration as desired.
title.classList.add("active");


$(document).ready(function () {
  $('.btnIcon').on('click', function () {
    $('nav ul').toggleClass('show');
  });

  $('nav li').on('click', function () {
    $('header nav ul').removeClass('show');
  });
});


