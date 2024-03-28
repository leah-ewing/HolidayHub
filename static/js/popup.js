'use strict';

// Pop-up window script

const popupWindow = document.getElementById("popup-window")
const shareWindow = document.getElementById("share-popup-window")
const popupWindowBox = document.getElementsByClassName("popup-window")

const popupButton = document.getElementById("popup-button")
const closeButton = document.getElementById("close-button")
const submitButton = document.getElementById("submit-button")
const closeButton_X = document.getElementById("x-close-enter-email")

const thankYouWindow = document.getElementById("thank-you-window")
const closeButtonThankYou = document.getElementById("close-button-thank-you")
const closeButtonThankYou_X = document.getElementById("x-close-thank-you")

const duplicateEmailWindow = document.getElementById("duplicate-email-window")
const closeButtonDuplicateEmail = document.getElementById("close-button-duplicate-email")
const closeButtonDuplicateEmail_X = document.getElementById("x-close-duplicate-email")
const tryAgainButton = document.getElementById("try-again-button")

const invalidEmailWindow = document.getElementById("invalid-email-window")
const closeButtonInvalidEmail = document.getElementById("close-button-invalid-email")
const closeButtonInvalidEmail_X = document.getElementById("x-close-invalid-email")
const tryAgainButtonInvalidEmail = document.getElementById("try-again-button-invalid-email")


popupButton.addEventListener("click", function(evt) {
    evt.preventDefault()
    evt.stopPropagation()
    
    shareWindow.style.display = "none"
    popupWindow.style.display = "block"
})

closeButton.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButton_X.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButtonDuplicateEmail.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButtonDuplicateEmail_X.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButtonInvalidEmail.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButtonInvalidEmail_X.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButtonThankYou.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

closeButtonThankYou_X.addEventListener("click", function() {
    closePopUps()

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

tryAgainButton.addEventListener("click", function() {
    duplicateEmailWindow.style.display = "none"
    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""
})

tryAgainButtonInvalidEmail.addEventListener("click", function() {
    invalidEmailWindow.style.display = "none"
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
            console.error(responseJson.memo, responseJson.status)
            duplicateEmailWindow.style.display = "block"
      } else if (responseJson.status == 400) {
            console.error(responseJson.memo, responseJson.status)
            invalidEmailWindow.style.display = "block"
      }
    })
})

document.addEventListener("click", function(evt) {
    evt.preventDefault()

    if (!evt.target.closest(".popup-window")) {
        closePopUps()
    }
})

function closePopUps() {
    popupWindow.style.display = "none"
    shareWindow.style.display = "none"
    thankYouWindow.style.display = "none"
    invalidEmailWindow.style.display = "none"
    duplicateEmailWindow.style.display = "none"
}