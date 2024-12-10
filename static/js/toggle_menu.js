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

  // Optional: To ensure the icon changes when the collapse state changes
  document.addEventListener('DOMContentLoaded', function () {
      const navbar = document.getElementById('navbarNav');
      const bsCollapse = new bootstrap.Collapse(navbar);

      // Listen for the collapse event
      navbar.addEventListener('shown.bs.collapse', function () {
          document.getElementById('menuIcon').src = "/static/icons/close.png";
      });

      navbar.addEventListener('hidden.bs.collapse', function () {
          document.getElementById('menuIcon').src = "/static/icons/menu.png";
      });
  });