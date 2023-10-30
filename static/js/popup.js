'use strict';

// Pop-up window script

const popupButton = document.getElementById("popup-button")
const popupWindow = document.getElementById("popup-window")
const closeButton = document.getElementById("close-button")

// Show the pop-up window when the link is clicked
popupButton.addEventListener("click", function(event) {
    event.preventDefault()
    popupWindow.style.display = "block"
})

// Hide the pop-up window when the close button is clicked
closeButton.addEventListener("click", function() {
    popupWindow.style.display = "none"
})