'use strict';

// Share button script

const shareButton = document.getElementById("share-button")
const sharePopUpWindow = document.getElementById("share-popup-window")
const closeButtonSharePopUpWindow = document.getElementById("share-close-button")

const twitterShareButton = document.getElementById("twitter-share-button")
const facebookShareButton = document.getElementById("facebook-share-button")
const pinterestShareButton = document.getElementById("pinterest-share-button")
const emailShareButton = document.getElementById("email-share-button")
const copyLinkButton = document.getElementById("copy-link-button")

shareButton.addEventListener("click", async () => {
    if (navigator.share) {
        try {
            await navigator.share({ title: "Example Page", url: "" })
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
    alert("twitter")
})

facebookShareButton.addEventListener("click", function() {
    alert("facebook")
})

pinterestShareButton.addEventListener("click", function() {
    alert("pinterest")
})

emailShareButton.addEventListener("click", function() {
    alert("email")
})

copyLinkButton.addEventListener("click", function() {
    alert("copy link")
})