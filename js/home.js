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
    // shuffle the divs in .reviews
    const reviewHighlights = document.querySelector(".review-highlights");
    for (let i = reviewHighlights.children.length; i >= 0; i--) {
        reviewHighlights.appendChild(reviewHighlights.children[Math.random() * i | 0]);
    }

    const reviews = document.querySelector(".reviews");
    for (let i = reviews.children.length; i >= 0; i--) {
        reviews.appendChild(reviews.children[Math.random() * i | 0]);
    }
});


