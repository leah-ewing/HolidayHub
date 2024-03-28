'use strict';

let nav = document.querySelector('#navbar')
      let lastScrollTop

      window.addEventListener("scroll", function() {
        var position = window.pageYOffset || document.documentElement.scrollTop;
        if (position > lastScrollTop) 
          nav.style.opacity = 0 // hide the nav-bar when going down
        else 
          nav.style.opacity = 1 // display the nav-bar when going up
        
        lastScrollTop = position

        nav.style.top = `${position}px` // set the position of the nav-bar to the current scroll
      }, false)