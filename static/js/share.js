'use strict';

// Share button script

const shareButton = document.getElementById("share-button")
const sharePopUpWindow = document.getElementById("share-popup-window")
const closeButtonSharePopUpWindow = document.getElementById("share-close-button")

shareButton.addEventListener("click", async () => {
    if (navigator.share) {
        try {
            await navigator.share({ title: "Example Page", url: "" })
            console.log("Data was shared successfully")
        } catch (err) {
            console.error("Share failed:", err.message)
        }
    } else {
        // alert("test")
        sharePopUpWindow.style.display = "block"
    }
})

closeButtonSharePopUpWindow.addEventListener("click", function() {
    sharePopUpWindow.style.display = "none"
})