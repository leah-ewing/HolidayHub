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
    // const individualHoliday = document.querySelector(".slideshow-holiday")
    // const transitionDuration = 500;

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

        holidaysDiv.innerHTML += (`<div class="col slideshow-holiday" id="slideshow-holiday-${i}">
                                        <div class="row slideshow-row">
                                            <div class="col" id="slideshow-holiday-image">
                                                <div class="image-container">
                                                    <img
                                                        src = "${slideshowHolidayList[i].holiday_img}"
                                                        width = 200
                                                        id = "slideshow-image">
                                                    </img>
                                                </div>
                                            </div>
                                        <div class="col" id="slideshow-holiday-blurb">
                                            <p id="slideshow-holiday-name">
                                                <span id="name-tag-${i}">
                                                    ${slideshowHolidayList[i].holiday_name}
                                                </span>
                                            </p>
                                            <p id="slideshow-holiday-date">
                                                ${slideshowHolidayList[i].holiday_month} ${slideshowHolidayList[i].holiday_date}${slideshowHolidayList[i].date_suffix}
                                            </p>
                                        </div>
                                    </div>`)
    }

    // individualHoliday.style.transition = `transform ${transitionDuration}ms ease`;
    // individualHoliday.style.transform = `translateX(-${first * 100}%)`;

    for (let i = 0; i < 3; i++) {
        let clickableSlideshowDiv = document.getElementById(`slideshow-holiday-${i}`)
        let slideshowHolidayName = document.getElementById(`name-tag-${i}`).innerHTML.trim()
        let url = `/${slideshowHolidayName}`

        clickableSlideshowDiv.addEventListener("click", function() {
            window.location.href = url
        })
    }
}

getSlideshowHolidays().then(() => holidaySlideshow())