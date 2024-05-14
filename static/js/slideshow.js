'use strict';

let slideshowHolidayList = []
let currentIndex = 0

const leftArrowButton = document.getElementById("left-arrow")
const rightArrowButton = document.getElementById("right-arrow")

leftArrowButton.addEventListener("click", function(evt) {
    evt.preventDefault()
    currentIndex = (currentIndex === 0) ? slideshowHolidayList.length - 1 : currentIndex - 1
    updateSlideshow()
})

rightArrowButton.addEventListener("click", function(evt) {
    evt.preventDefault()
    currentIndex = (currentIndex === slideshowHolidayList.length - 1) ? 0 : currentIndex + 1
    updateSlideshow()
})

async function getSlideshowHolidays() {
    return fetch("/get-slideshow-holidays")
        .then((response) => response.json())
        .then((slideshow_holidays) => {
            slideshowHolidayList = slideshow_holidays
            updateSlideshow()
        })
}

async function loadNextHolidays() {
    const nextIndex = (currentIndex + 3) % slideshowHolidayList.length
    await fetch(`/get-slideshow-holidays?start=${nextIndex}&count=3`)
        .then((response) => response.json())
        .then((next_holidays) => {
            slideshowHolidayList = slideshowHolidayList.concat(next_holidays)
        })
}

async function updateSlideshow() {
    const holidaysDiv = document.getElementById("holidays")
    holidaysDiv.innerHTML = ""

    const startIndex = currentIndex
    const endIndex = (currentIndex + 2) % slideshowHolidayList.length

    for (let i = startIndex; i <= endIndex; i++) {
        const index = i % slideshowHolidayList.length
        const holiday = slideshowHolidayList[index]
        holidaysDiv.innerHTML += `<div class="col slideshow-holiday inner-row width-100 pointer-cursor hover-div" onclick="location.href='/${holiday.holiday_name}'">
                                    <div class="row slideshow-row">
                                        <div class="col grid-center" id="slideshow-holiday-image">
                                            <div class="image-container">
                                                <img src="${holiday.holiday_img}" width="200" id="slideshow-image" class="brightened-image">
                                                </img>
                                            </div>
                                        </div>
                                        <div class="col" id="slideshow-holiday-blurb">
                                            <p id="slideshow-holiday-name">
                                                <span id="name-tag-${index}">
                                                    ${holiday.holiday_name}
                                                </span>
                                            </p>
                                            <p id="slideshow-holiday-date" class="pink-text">
                                                ${holiday.holiday_month} ${holiday.holiday_date}${holiday.date_suffix}
                                            </p>
                                        </div>
                                    </div>
                                </div>`
    }

    if (endIndex + 1 === slideshowHolidayList.length) {
        await loadNextHolidays()
    }
}

getSlideshowHolidays()