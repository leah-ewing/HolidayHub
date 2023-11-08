'use strict';

// Share button script

const shareButton = document.getElementById("share-button")
const sharePopUpWindow = document.getElementById("share-popup-window")
const closeButtonSharePopUpWindow = document.getElementById("share-close-button")

const thankYouForSharingPopUpWindow = document.getElementById("thank-you-for-sharing-window")
const closeButtonThankYouForSharing = document.getElementById("close-button-thank-you-for-sharing")

const twitterShareButton = document.getElementById("twitter-share-button")
const facebookShareButton = document.getElementById("facebook-share-button")
const pinterestShareButton = document.getElementById("pinterest-share-button")
const emailShareButton = document.getElementById("email-share-button")
const copyLinkButton = document.getElementById("copy-link-button")

shareButton.addEventListener("click", async () => {
    if (navigator.share) {
        try {
            await navigator.share({ url: "" })
            console.log("Data was shared successfully")
        } catch (err) {
            console.error("Share failed:", err.message)
        }
    } else {
        sharePopUpWindow.style.display = "block"
    }
})

closeButtonSharePopUpWindow.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
})

twitterShareButton.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

facebookShareButton.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

pinterestShareButton.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

emailShareButton.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
    thankYouForSharingPopUpWindow.style.display = "block"
})

copyLinkButton.addEventListener("click", function() {
    copyToClipboard(window.location.href);
})

closeButtonThankYouForSharing.addEventListener("click", function() {
    thankYouForSharingPopUpWindow.style.display = "none"
})

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
        document.execCommand('copy');
        console.log('Link copied to clipboard')
        alert('Link copied!')
    } catch (err) {
        console.error('Unable to copy to clipboard', err)
    } finally {
        document.body.removeChild(tempElement);
    }
}