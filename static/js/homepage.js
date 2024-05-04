'use strict';

// Homepage Holiday Display Script

async function getHomepageHoliday() {
    const date_now = new Date
    const month = date_now.getMonth() + 1
    const day = date_now.getDate()
    const year = date_now.getFullYear()

    const current_date = {'current_date': `${year}-${month}-${day}`}

    fetch('/get-homepage-holiday', {
        method: 'POST',
        body: JSON.stringify(current_date),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((homepageHoliday) => {

        const homepageHolidayDisplayDiv = document.getElementById('today-is-inner-row')

        homepageHolidayDisplayDiv.innerHTML = `<div class="col inner-row" id="today-is-text-col">
                                                    <text id="today-is-text">
                                                        <b>
                                                            Today is...
                                                        </b>
                                                    </text>

                                                    <text class="holiday-name">
                                                        <b>
                                                            ${homepageHoliday.holiday_name}!
                                                        </b>
                                                    </text>

                                                    <div id="learn-more-button-span">
                                                        <button id="learn-more-button" class="btn pink-button" onclick="location.href='/${homepageHoliday.holiday_name}'">
                                                            Learn more
                                                        </button>
                                                    </div>
                                                </div>

                                                <div class="col grid-center inner-row" id="homepage-image">
                                                    <a href="/${homepageHoliday.holiday_name}">
                                                        <div class="image-container">
                                                            <img
                                                                class = "homepage-image brightened-image sized-image"
                                                                src = "${homepageHoliday.holiday_img}"
                                                                width = 400>
                                                            </img>
                                                        </div>
                                                    </a>
                                                </div>`

    })
}

getHomepageHoliday()