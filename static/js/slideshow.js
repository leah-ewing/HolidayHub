'use strict';

// 'Explore More Holidays...' Slideshow Script

let slideshowHolidayList = []

let firstHolidayIndex
let secondHolidayIndex
let thirdHolidayIndex

const leftArrowButton = document.getElementById("left-arrow")
const rightArrowButton = document.getElementById("right-arrow")


leftArrowButton.addEventListener("click", function(evt) {
    evt.preventDefault()

    const holidaysDiv = document.getElementById("holidays")
    holidaysDiv.innerHTML = ""

    holidaySlideshow(firstHolidayIndex-1, secondHolidayIndex-1, thirdHolidayIndex-1, true)
})


rightArrowButton.addEventListener("click", function(evt) {
    evt.preventDefault()

    const holidaysDiv = document.getElementById("holidays")
    holidaysDiv.innerHTML = ""

    holidaySlideshow(firstHolidayIndex+1, secondHolidayIndex+1, thirdHolidayIndex+1, true)
})


async function getSlideshowHolidays() {
    return fetch("/get-slideshow-holidays")
        .then((response) => response.json())
        .then((slideshow_holidays) => {
            slideshowHolidayList = slideshow_holidays
        })
}


async function holidaySlideshow(first=0, second=1, third=2, continuing=false) {
    const holidaysDiv = document.getElementById("holidays")

    if (continuing == false) {
        await getSlideshowHolidays()
    } 
    
    else if (third == slideshowHolidayList.length) {
        third = 0
    } else if (second == slideshowHolidayList.length) {
        second = 0
    } else if (first == slideshowHolidayList.length) {
        first = 0
    }

    else if (first == -1) {
        first = slideshowHolidayList.length - 1
    } else if (second == -1) {
        second = slideshowHolidayList.length -1
    } else if (third == -1) {
        third = slideshowHolidayList.length - 1
    }

    firstHolidayIndex = first
    secondHolidayIndex = second
    thirdHolidayIndex = third

    let slideshowHolidayIndexes = [firstHolidayIndex, secondHolidayIndex, thirdHolidayIndex]

    for (let i of slideshowHolidayIndexes) {
        holidaysDiv.innerHTML += (`<div class="col" id="slideshow-holiday">
                                        <div class="row">
                                            <div class="col" id="slideshow-holiday-image">
                                                <a href = "/${slideshowHolidayList[i].holiday_name}">
                                                    <div class="image-container">
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