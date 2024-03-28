'use strict';

let nav = document.querySelector('#navbar')
let lastScrollTop

window.addEventListener("scroll", function() {
  let position = window.pageYOffset || document.documentElement.scrollTop

  if (position > lastScrollTop && document.documentElement.scrollTop > 50)  {
    nav.style.opacity = 0 // hide the nav-bar when going down
  } else {
    nav.style.opacity = 1 // display the nav-bar when going up
  } 

  lastScrollTop = position
})