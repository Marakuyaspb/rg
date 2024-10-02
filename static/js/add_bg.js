function add_bg() {
    const navbarNav = document.getElementById("navbarNav");
    const nav_mob = document.getElementById("nav_mob");

    setTimeout(function() {
        if (navbarNav.classList.contains("show")) {
            console.log("yes")
            nav_mob.classList.add("white_dirty_bg");
        } else {
            nav_mob.classList.remove("white_dirty_bg");
            console.log("no")
        }
    }, 400); 
}