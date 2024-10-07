document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card');
    let delay = 0;

    cards.forEach((card) => {
        setTimeout(() => {
            card.style.opacity = 1; // Fade in effect
        }, delay);
        delay += 200; // Adjust delay as needed for effect
    });
});
