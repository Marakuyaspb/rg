document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById('menuIcon');
    const navbar = document.getElementById('navbarNav');

    // Set the initial icon to the menu icon
    menuIcon.src = "/static/icons/menu.png";

    // Ensure the navbar is collapsed on page load
    if (navbar.classList.contains('show')) {
        navbar.classList.remove('show');
    }

    // Listen for collapse events to update the icon
    navbar.addEventListener('shown.bs.collapse', function () {
        menuIcon.src = "/static/icons/close.png";
    });

    navbar.addEventListener('hidden.bs.collapse', function () {
        menuIcon.src = "/static/icons/menu.png";
    });
});

// Function to toggle the menu icon when clicked
function toggleMenuIcon() {
    const menuIcon = document.getElementById('menuIcon');
    const navbar = document.getElementById('navbarNav');

    // Check if the navbar is currently expanded
    if (navbar.classList.contains('show')) {
        // If expanded, change to close icon
        menuIcon.src = "/static/icons/close.png";
    } else {
        // If collapsed, change back to menu icon
        menuIcon.src = "/static/icons/menu.png";
    }
}