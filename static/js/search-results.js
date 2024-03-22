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
                                            <a id="search-result-name-${result.result_num}" href="/${result.holiday_name}">${result.holiday_name}</a>
                                            <div class="row">
                                                <div class="col" id="search-result-image">
                                                    <a href="/${result.holiday_name}">
                                                        <div class="image-container">
                                                            <img
                                                                src = "${result.holiday_img}"
                                                                width = 200,
                                                                id = "search-result-img">
                                                            </img>
                                                        </div>
                                                    </a>
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

}

displaySearchResults()