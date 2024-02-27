'use strict';

let slideshowHolidayList = []

let startIndex
let endIndex

const leftArrowButton = document.getElementById("left-arrow")
const rightArrowButton = document.getElementById("right-arrow")


rightArrowButton.addEventListener("click", function(evt) {
    evt.preventDefault()

    const holidaysDiv = document.getElementById("holidays")
    holidaysDiv.innerHTML = ""

    holidaySlideshow(startIndex+1, endIndex+1)
    // add if first index
})


leftArrowButton.addEventListener("click", function(evt) {
    evt.preventDefault()

    const holidaysDiv = document.getElementById("holidays")
    holidaysDiv.innerHTML = ""

    holidaySlideshow(startIndex-1, endIndex-1)
    // add if last index
})


async function getSlideshowHolidays() {
    return fetch(`/get-slideshow-holidays`)
        .then((response) => response.json())
        .then((slideshow_holidays) => {
            slideshowHolidayList = slideshow_holidays
        })
}


async function holidaySlideshow(start=0, end=2) {
    startIndex = start
    endIndex = end

    await getSlideshowHolidays()

    const holidaysDiv = document.getElementById("holidays")

    for (let i = start; i <= end; i++) {
        holidaysDiv.innerHTML += (`<div class="col" id="slideshow-holiday">
                                        <div class="row">
                                            <div class="col" id="slideshow-holiday-image">
                                                <a href = "/${slideshowHolidayList[i].holiday_name}">
                                                <div class="image-container" id="slideshow-image">
                                                    <img
                                                        src = "${slideshowHolidayList[i].holiday_img}"
                                                        width = 200
                                                        id = "slideshow-image">
                                                    </img>
                                                </div>
                                                </a>
                                            </div>
                                        <div class="col" id="slideshow-holiday-blurb">
                                            <p id="slideshow-holiday-name">
                                                <a href="/${slideshowHolidayList[i].holiday_name}" id="name-tag">
                                                    ${slideshowHolidayList[i].holiday_name}
                                                </a>
                                            </p>
                                            <p id="slideshow-holiday-date">
                                                ${slideshowHolidayList[i].holiday_month} ${slideshowHolidayList[i].holiday_date}${slideshowHolidayList[i].date_suffix}
                                            </p>
                                        </div>
                                    </div>`)
    }
}

getSlideshowHolidays().then(() => holidaySlideshow())