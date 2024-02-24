'use strict';

const leftArrowButton = document.getElementById("left-arrow")
const rightArrowButton = document.getElementById("right-arrow")


async function holidaySlideshow() {

    const holidaysDiv = document.getElementById("holidays")

    fetch('/get-slideshow-holidays')
    .then((response) => response.json())
    .then((slideshow_holidays) => {

        for (let holiday of slideshow_holidays) {
            holidaysDiv.innerHTML += (`<div class="col" id="slideshow-holiday">
                                            <div class="row">
                                                <div class="col" id="slideshow-holiday-image">
                                                    <a href = "/${holiday.holiday_name}">
                                                    <div class="image-container" id="slideshow-image">
                                                        <img
                                                            src = "${holiday.holiday_img}"
                                                            width = 200
                                                            id = "slideshow-image">
                                                        </img>
                                                    </div>
                                                    </a>
                                                </div>
                                            <div class="col" id="slideshow-holiday-blurb">
                                                <p id="slideshow-holiday-name">
                                                    <a href="/${holiday.holiday_name}" id="name-tag">
                                                        ${holiday.holiday_name}
                                                    </a>
                                                </p>
                                                <p id="slideshow-holiday-date">
                                                    ${holiday.holiday_month} ${holiday.holiday_date}${holiday.date_suffix}
                                                </p>
                                            </div>
                                        </div>`)
        }
    })
}

holidaySlideshow()