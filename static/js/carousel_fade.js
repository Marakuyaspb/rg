let slideIndexFade = 1;
showSlides();

function plusSlides(n) {
  showSlides(slideIndexFade += n);
}

function currentSlide(n) {
  showSlides(slideIndexFade = n);
}

function showSlides(n) {
  let slides = document.getElementsByClassName("carousel_slide_fade");
  let indicators = document.getElementsByClassName("indicator");

  
  if (n > slides.length) {
    slideIndexFade = 1;
  }
  
  if (n < 1) {
    slideIndexFade = slides.length;
  }
  
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    slides[i].classList.remove("fade_it");
    indicators[i].classList.remove("active");
  }
  
  slides[slideIndexFade - 1].style.display = "block";
  slides[slideIndexFade - 1].classList.add("fade_it");
  indicators[slideIndexFade - 1].classList.add("active"); 
}

setTimeout(function() {
  plusSlides(1);
}, 5000);