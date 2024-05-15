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

async function getSlideshowHolidays(startIndex, count) {
    return fetch(`/get-slideshow-holidays?start=${startIndex}&count=${count}`)
        .then((response) => response.json())
        .then((slideshow_holidays) => {
            return slideshow_holidays
        })
}

async function loadNextHolidays() {
    const nextIndex = (currentIndex + 3) % slideshowHolidayList.length
    const nextHolidays = await getSlideshowHolidays(nextIndex, 3)
    slideshowHolidayList = slideshowHolidayList.concat(nextHolidays)
}

async function updateSlideshow() {
    const holidaysDiv = document.getElementById("holidays")
    holidaysDiv.innerHTML = ""

    const currentIndexMod = currentIndex % slideshowHolidayList.length
    const prevIndex = (currentIndexMod === 0) ? slideshowHolidayList.length - 1 : currentIndexMod - 1
    const nextIndex = (currentIndexMod === slideshowHolidayList.length - 1) ? 0 : currentIndexMod + 1

    const slideshowItems = [
        slideshowHolidayList[prevIndex],
        slideshowHolidayList[currentIndexMod],
        slideshowHolidayList[nextIndex]
    ]

    for (const holiday of slideshowItems) {
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
                                                <span id="name-tag-${holiday.index}">
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

    if (nextIndex === 0) {
        await loadNextHolidays()
    }
}

async function initializeSlideshow() {
    const initialHolidays = await getSlideshowHolidays(0, 3)
    slideshowHolidayList = initialHolidays
    updateSlideshow()
}

initializeSlideshow()