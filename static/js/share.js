'use strict';

// Share button script

let shareButton = document.getElementById("share-button")

shareButton.addEventListener("click", async () => {
    if (navigator.share) {
        try {
            await navigator.share({ title: "Example Page", url: "" })
            console.log("Data was shared successfully")
        } catch (err) {
            console.error("Share failed:", err.message)
        }
    } else {
        alert("test")
    }
})