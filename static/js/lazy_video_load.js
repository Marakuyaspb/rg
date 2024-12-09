document.addEventListener("DOMContentLoaded", function() {
    const videos = document.querySelectorAll('video[data-src]');

    const options = {
        root: null, // Use the viewport as the container
        threshold: 0.1 // Trigger when 10% of the video is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const video = entry.target;
                const source = video.querySelector('source');
                source.src = video.getAttribute('data-src');
                video.load(); // Load the video
                video.play(); // Start playing the video
                observer.unobserve(video); // Stop observing once loaded
            }
        });
    }, options);

    videos.forEach(video => {
        observer.observe(video);
    });
});