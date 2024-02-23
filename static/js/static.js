'use strict';

// Animated Homepage Title Script

async function init () {
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
  
  init()