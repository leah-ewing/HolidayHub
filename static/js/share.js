'use strict';

// Share button script

const shareButton = document.getElementById("share-button")
const sharePopUpWindow = document.getElementById("share-popup-window")
const closeButtonSharePopUpWindow = document.getElementById("share-close-button")
const closeButtonSharePopUpWindow_X = document.getElementById("x-close-share")

const thankYouForSharingPopUpWindow = document.getElementById("thank-you-for-sharing-window")
const closeButtonThankYouForSharing = document.getElementById("close-button-thank-you-for-sharing")
const closeButtonThankYouForSharing_X = document.getElementById("x-close-thank-you-for-sharing")

const twitterShareButton = document.getElementById("twitter-share-button")
const facebookShareButton = document.getElementById("facebook-share-button")
const pinterestShareButton = document.getElementById("pinterest-share-button")
const emailShareButton = document.getElementById("email-share-button")
const copyLinkButton = document.getElementById("copy-link-button")

const htmlBody = document.body


shareButton.addEventListener("click", async () => {
    if (navigator.share) {
        try {
            await navigator.share({ url: "" })
            console.log("Data was shared successfully")
        } catch (err) {
            console.error("Share failed:", err.message)
        }
    } else {
        popupWindow.style.display = "none"
        sharePopUpWindow.style.display = "block"
    }
})

closeButtonSharePopUpWindow.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
    document.getElementById("link-copied-label").innerHTML = ""
})

closeButtonSharePopUpWindow_X.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
    document.getElementById("link-copied-label").innerHTML = ""
})

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

closeButtonThankYouForSharing.addEventListener("click", function() {
    thankYouForSharingPopUpWindow.style.display = "none"
})

closeButtonThankYouForSharing_X.addEventListener("click", function() {
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
        document.execCommand('copy')
        console.log('Link copied to clipboard')
    } catch (err) {
        console.error('Unable to copy to clipboard', err)
    } finally {
        document.body.removeChild(tempElement)
    }
}