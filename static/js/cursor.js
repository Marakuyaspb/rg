let cursor = document.querySelector('.cursor');
let follower = document.querySelector('.follower');

document.addEventListener('mousemove', (e) => {
    cursor.style.left = `${e.pageX}px`;
    cursor.style.top = `${e.pageY}px`;

    follower.style.left = `${e.pageX - 15}px`;
    follower.style.top = `${e.pageY - 15}px`;
});