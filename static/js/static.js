'use strict';

// Navbar Script

let throttling = false;

function onScrollThrottled() {
  if (!throttling) {
    throttling = true;
    requestAnimationFrame(() => {
      onScroll();
      throttling = false;
    });
  }
}

let navbarTop = 0;
let transition = true;
let position = "absolute";
let lastScrollPosition = 0;

const navbar = document.getElementById("navbar");

function onScroll() {

  const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop;

  if (currentScrollPosition <= 0) {

    lastScrollPosition = 0;
    navbarTop = 0;

    if (position !== "absolute") { transition = true; }
    else { transition = false; }
    position = "absolute";

  } else {
    
    if (currentScrollPosition > lastScrollPosition) {

      if (position !== "absolute") { transition = true; }
      else { transition = false; }
      position = "absolute";

      let { top, height } = navbar.getBoundingClientRect()
      navbarTop = currentScrollPosition + Math.max(top, -height);

    } else {

      const { top } = navbar.getBoundingClientRect()

      if (top >= 0) {

        navbarTop = 0;

        if (position !== "fixed") { transition = true; }
        else { transition = false; }
        position = "fixed";

      }

    }

    lastScrollPosition = currentScrollPosition;

  }
  navbar.style = `position: ${position}; top: ${navbarTop}px; transition: ${ transition ? "none" : "100ms linear" }`;
}

window.addEventListener("scroll", onScrollThrottled, { passive: true });


// Animated Homepage Title Script

async function animatedTitle () {
    const node = document.querySelector("#celebrate-dynamic")
    
    await sleep(2000)
    await node.delete(node.innerHTML)

    const title_words = ['Gather', 'Party', 'Dance', 'Laugh', 'Chat', 'Love']

    while (true) {
        for (let word of title_words) {
            await node.type(word)
            await sleep(2000)
            await node.delete(word)
        }
    }
  }

  const sleep = time => new Promise(resolve => setTimeout(resolve, time))
  
  class TypeAsync extends HTMLSpanElement {
    get typeInterval () {
      const randomMs = 100 * Math.random()
      return randomMs < 50 ? 10 : randomMs
    }
    
    async type (text) {
      for (let character of text) {
        this.innerText += character
        await sleep(this.typeInterval)
      }
    }
    
    async delete (text) {
      for (let character of text) {
        this.innerText = this.innerText.slice(0, this.innerText.length -1)
        await sleep(this.typeInterval)
      }
    }
  }
  
  customElements.define('type-async', TypeAsync, { extends: 'span' })
  
  animatedTitle()