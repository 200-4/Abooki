// Select all elements with the class 'section-title'
const animatedElements = document.querySelectorAll('.section-title');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // When the element is in view, add the 'is-visible' class
            entry.target.classList.add('is-visible');
            // Stop observing the element so the animation only runs once
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5 // Adjust this value (0.0 to 1.0) to control when the animation triggers
});

// Loop over each element and start observing it
animatedElements.forEach(element => {
    observer.observe(element);
});