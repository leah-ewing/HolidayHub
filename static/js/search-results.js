'use strict';

// Search Results Script


async function makeSearchResultsClickable() {

    let searchResults

    const searchTerm = document.getElementById("search-term").innerHTML.trim()

    await fetch(`/get-search-results/${searchTerm}`)
            .then((response) => response.json())
            .then((search_results) => {
                searchResults = search_results
            })

    for (let i = 1; i < searchResults.length + 1; i++) {
        let clickableSearchResultDiv = document.getElementById(`search-result-${i}`)
        let slideshowHolidayName = document.getElementById(`search-result-name-${i}`).innerHTML.trim()
        console.log(slideshowHolidayName)
        let url = `/${slideshowHolidayName}`

        clickableSearchResultDiv.addEventListener("click", function() {
            window.location.href = url
        })
    }

}

makeSearchResultsClickable()