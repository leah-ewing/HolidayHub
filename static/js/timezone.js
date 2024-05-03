'use strict';

// Local Timezone Script

function getCurrentDateInUserTimezone() {
    const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone
    const currentDate = new Date().toLocaleDateString(undefined, { timeZone: userTimezone })
    return currentDate
}

function returnCurrentDateInUserTimezone() {
    const current_date_in_user_timezone = getCurrentDateInUserTimezone()
    const url = `/get-current-date?current_date=${current_date_in_user_timezone}`

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
}

returnCurrentDateInUserTimezone()