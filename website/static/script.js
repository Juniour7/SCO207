const hamburgerToggle =document.querySelector("#hamburger-toggle");
const nav_bar = document.querySelector("#nav-bar");
hamburgerToggle.addEventListener("click", onHamburgerClick);

function onHamburgerClick() {
  if (!nav_bar.classList.contains("open")){
    nav_bar.classList.add("open");
  } else{
  nav_bar.classList.remove("open");
  }
}

const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};

ScrollReveal().reveal(".header_img img", {
  ...scrollRevealOption,
  origin: "top",
});
ScrollReveal().reveal(".header_content h2", {
  ...scrollRevealOption,
  origin: "left",
  delay: 500,
});
ScrollReveal().reveal(".header_content h1", {
  ...scrollRevealOption,
  delay: 900,
});

scrollReveal().reveal(".order_card", {
  ...scrollRevealOption,
  interval: 500,
});