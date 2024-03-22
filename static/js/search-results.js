'use strict';

// Search Results Script


async function displaySearchResults() {

    let searchResults

    const searchResultsDiv = document.getElementById("search-results-list")
    const searchTerm = document.getElementById("search-term").innerHTML.trim()

    await fetch(`/get-search-results/${searchTerm}`)
            .then((response) => response.json())
            .then((search_results) => {
                searchResults = search_results
            })

    for (let result of searchResults) {

        searchResultsDiv.innerHTML += `<div class="row search-result" id="search-result-${result.result_num}">
                                            <text class="search-result-name" id="search-result-name-${result.result_num}" href="/${result.holiday_name}">
                                            ${result.holiday_name}
                                            </text>
                                            <div class="row">
                                                <div class="col" id="search-result-image">
                                                    <span href="/${result.holiday_name}">
                                                        <div class="image-container">
                                                            <img
                                                                src = "${result.holiday_img}"
                                                                width = 200,
                                                                id = "search-result-img">
                                                            </img>
                                                        </div>
                                                    </span>
                                                </div>
                                                <div class="col" id="search-result-blurb">
                                                    <text>
                                                        <div id="search-result-date">
                                                            ${result.holiday_month} ${result.holiday_date}${result.date_suffix}
                                                        </div>
                                                        ${result.holiday_blurb} <b>...</b>
                                                    </text>
                                                </div>
                                            </div>
                                        </div>`
    }

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

displaySearchResults()