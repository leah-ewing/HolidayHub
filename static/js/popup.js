'use strict';

// Pop-up window script


let popupOpen = false


// Close popups when clicking off
document.addEventListener("click", function(evt) {
    if (!evt.target.closest(".popup-window") && popupOpen == true) {
        closePopUps()
    }
})


// Copy Link button logic
function copyToClipboard(text) {
    const tempElement = document.createElement('div')
    tempElement.contentEditable = true
    tempElement.innerHTML = text

    tempElement.style.position = 'absolute'
    tempElement.style.left = '-9999px'

    document.body.appendChild(tempElement)
    
    const range = document.createRange()
    range.selectNodeContents(tempElement)
    const selection = window.getSelection()
    selection.removeAllRanges()
    selection.addRange(range)

    try {
        document.execCommand('copy')
        console.log('Link copied to clipboard')
    } catch (err) {
        console.error('Unable to copy to clipboard', err)
    } finally {
        document.body.removeChild(tempElement)
    }
}


// Closes all popups
function closePopUps() {
    popupWindow.style.display = "none"
    sharePopUpWindow.style.display = "none"
    thankYouWindow.style.display = "none"
    invalidEmailWindow.style.display = "none"
    duplicateEmailWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "none"

    document.getElementById("fname").value = ""
    document.getElementById("email").value = ""

    popupOpen = false
}


// Email Sign-Up Popup

// Submission form
const popupWindow = document.getElementById("popup-window") 

const popupButton = document.getElementById("popup-button")
const popupButtonPhone = document.getElementById("popup-button-phone")

const closeButton = document.getElementById("close-button")
const submitButton = document.getElementById("submit-button")
const closeButton_X = document.getElementById("x-close-enter-email")

document.addEventListener("DOMContentLoaded", function() {
    const calendarViewSignUpButton = document.getElementById("sign-up-button")

    if (calendarViewSignUpButton) {
        calendarViewSignUpButton.addEventListener("click", function(evt) {
            evt.preventDefault()

            if (!popupOpen) {
                sharePopUpWindow.style.display = "none"
                popupWindow.style.display = "block"

                popupOpen = true
            }

            evt.stopPropagation()
        })
    }
})

popupButton.addEventListener("click", function(evt) {

    if (!popupOpen) {
        popupWindow.style.display = "block";
        popupOpen = true;

    } else {
        closePopUps()
        popupWindow.style.display = "block";
        popupOpen = true;
    }

    evt.stopPropagation();
});

popupButtonPhone.addEventListener("click", function(evt) {

    if (!popupOpen) {
        popupWindow.style.display = "block";
        popupOpen = true;

    } else {
        closePopUps()
        popupWindow.style.display = "block";
        popupOpen = true;
    }

    evt.stopPropagation();
});

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


// Thank you for submitting
const thankYouWindow = document.getElementById("thank-you-window")

const closeButtonThankYou = document.getElementById("close-button-thank-you")
const closeButtonThankYou_X = document.getElementById("x-close-thank-you")

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


// Duplicate email
const duplicateEmailWindow = document.getElementById("duplicate-email-window")

const closeButtonDuplicateEmail = document.getElementById("close-button-duplicate-email")
const closeButtonDuplicateEmail_X = document.getElementById("x-close-duplicate-email")
const tryAgainButton = document.getElementById("try-again-button")

tryAgainButton.addEventListener("click", function() {
    duplicateEmailWindow.style.display = "none"
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


// Invalid email
const invalidEmailWindow = document.getElementById("invalid-email-window")

const tryAgainButtonInvalidEmail = document.getElementById("try-again-button-invalid-email")
const closeButtonInvalidEmail = document.getElementById("close-button-invalid-email")
const closeButtonInvalidEmail_X = document.getElementById("x-close-invalid-email")

tryAgainButtonInvalidEmail.addEventListener("click", function() {
    invalidEmailWindow.style.display = "none"
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


// Share Popup

// Share popup window
const sharePopUpWindow = document.getElementById("share-popup-window")

const shareButton = document.getElementById("share-button")
const shareButtonPhone = document.getElementById("share-button-phone")

const closeButtonSharePopUpWindow = document.getElementById("share-close-button")
const closeButtonSharePopUpWindow_X = document.getElementById("x-close-share")

shareButton.addEventListener("click", async(evt) => {
    if (navigator.share) {
        try {
            await navigator.share({ url: "" })
            console.log("Data was shared successfully")
        } catch (err) {
            console.error("Share failed:", err.message)
        }
    } else {
        evt.stopPropagation()
        
        popupWindow.style.display = "none"
        sharePopUpWindow.style.display = "block"

        popupOpen = true
    }
})

shareButtonPhone.addEventListener("click", async(evt) => {
    if (navigator.share) {
        try {
            await navigator.share({ url: "" })
            console.log("Data was shared successfully")
        } catch (err) {
            console.error("Share failed:", err.message)
        }
    } else {
        evt.stopPropagation()
        
        popupWindow.style.display = "none"
        sharePopUpWindow.style.display = "block"

        popupOpen = true
    }
})

closeButtonSharePopUpWindow.addEventListener("click", function() {
    closePopUps()

    document.getElementById("link-copied-label").innerHTML = ""
})

closeButtonSharePopUpWindow_X.addEventListener("click", function() {
    closePopUps()
    
    document.getElementById("link-copied-label").innerHTML = ""
})


// Share buttons
const twitterShareButton = document.getElementById("twitter-share-button")
const facebookShareButton = document.getElementById("facebook-share-button")
const pinterestShareButton = document.getElementById("pinterest-share-button")
const emailShareButton = document.getElementById("email-share-button")
const copyLinkButton = document.getElementById("copy-link-button")

twitterShareButton.addEventListener("click", function() {
    const currentUrl = window.location.href
    const twitterShareURL = "https://twitter.com/intent/tweet?url=" + encodeURIComponent(currentUrl)

    window.open(twitterShareURL, "_blank")

    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

facebookShareButton.addEventListener("click", function() {
    const currentUrl = window.location.href
    const facebookShareURL = "https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(currentUrl)

    window.open(facebookShareURL, "_blank")

    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

pinterestShareButton.addEventListener("click", function() {
    const currentUrl = window.location.href
    const pinterestSaveURL = "https://www.pinterest.com/pin/create/button/?url=" + encodeURIComponent(currentUrl)

    window.open(pinterestSaveURL, "_blank")

    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

emailShareButton.addEventListener("click", function() {
    const currentUrl = window.location.href
    const subject = "Check out this page!"
    const body = "I wanted to show you this! - " + currentUrl

    const mailtoLink = "mailto:?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body)
    window.location.href = mailtoLink

    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

copyLinkButton.addEventListener("click", function() {
    copyToClipboard(window.location.href)
    document.getElementById("link-copied-label").innerHTML = "Link Copied!"
})


// Thank you for sharing
const thankYouForSharingPopUpWindow = document.getElementById("thank-you-for-sharing-window")

const closeButtonThankYouForSharing = document.getElementById("close-button-thank-you-for-sharing")
const closeButtonThankYouForSharing_X = document.getElementById("x-close-thank-you-for-sharing")

closeButtonThankYouForSharing.addEventListener("click", function() {
    thankYouForSharingPopUpWindow.style.display = "none"
})

closeButtonThankYouForSharing_X.addEventListener("click", function() {
    thankYouForSharingPopUpWindow.style.display = "none"
})