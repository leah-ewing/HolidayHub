'use strict';

// Pop-up window script

const popupButton = document.getElementById("popup-button")
const popupWindow = document.getElementById("popup-window")
const closeButton = document.getElementById("close-button")
const submitButton = document.getElementById("submit-button")

const thankYouWindow = document.getElementById("thank-you-window")
const closeButtonThankYou = document.getElementById("close-button-thank-you")

const duplicateEmailWindow = document.getElementById("duplicate-email-window")
const closeButtonDuplicateEmail = document.getElementById("close-button-duplicate-email")
const tryAgainButton = document.getElementById("try-again-button")


popupButton.addEventListener("click", function(evt) {
    evt.preventDefault()
    popupWindow.style.display = "block"
})

closeButton.addEventListener("click", function() {
    popupWindow.style.display = "none"
    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButtonDuplicateEmail.addEventListener("click", function() {
    duplicateEmailWindow.style.display = "none"
    popupWindow.style.display = "none"
    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

tryAgainButton.addEventListener("click", function() {
    duplicateEmailWindow.style.display = "none"
    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

submitButton.addEventListener('click', (evt) => {
    evt.preventDefault()

    const formInputs = {
        fname: document.querySelector('#fname').value,
        email: document.querySelector('#email').value
    }

    fetch('/add-email', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
        'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((responseJson) => {
      if (responseJson.status == 200) {
        console.log(responseJson.memo, responseJson.status)
        thankYouWindow.style.display = "block"
      } else if (responseJson.status == 409) {
            console.log(responseJson.memo, responseJson.status)
            duplicateEmailWindow.style.display = "block"
      }
    })
})

closeButtonThankYou.addEventListener("click", function() {
    thankYouWindow.style.display = "none"
    popupWindow.style.display = "none"
    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})