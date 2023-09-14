const daysTag = document.querySelector(".days"),
currentDate = document.querySelector(".current-date"),
prevNextIcon = document.querySelectorAll(".icons span");

// Creating a new date and getting the current year and month
let date = new Date(),
currYear = date.getFullYear(),
currMonth = date.getMonth()

// Store months in an array
const months = ["January", "February", "March", "April", "May", "June", "July", 
                "August", "September", "October", "November", "December"]

const renderCalendar = () => {
    let firstDayofMonth = new Date(currYear, currMonth, 1).getDay(), // Get first day of month
    lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(), // Get last date of month
    lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(), // Get last day of month
    lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate() // Getting last date of previous month
    let liTag = ""

    // Create li of previous month last days
    for (let i = firstDayofMonth; i > 0; i--)
        liTag += `<li class="inactive">${lastDateofLastMonth - i + 1}</li>`

    // Create li of all days of current month
    for (let i = 1; i <= lastDateofMonth; i++) { 
        // Add active class to li if the current day, month, and year matched
        let isToday = i === date.getDate() && currMonth === new Date().getMonth() 
                        && currYear === new Date().getFullYear() ? "active" : ""
        liTag += `<li class="${isToday}">${i}</li>`
    }

    // Create li of next month first days
    for (let i = lastDayofMonth; i < 6; i++)
        liTag += `<li class="inactive">${i - lastDayofMonth + 1}</li>`

    // Pass current month and year as currentDate text
    currentDate.innerText = `${months[currMonth]} ${currYear}` 
    daysTag.innerHTML = liTag

    // Open booking time form when a day is clicked
    $('.days').click(function() {
        var dayClicked = this.className
        console.log("--" + dayClicked)
    
        if (dayClicked !== "inactive")
            openBookingTimeModal()
    })
}
renderCalendar()

// Get prev and next icons
prevNextIcon.forEach(icon => {
    // Add click event on both icons
    icon.addEventListener("click", () => { 
        // Increment or decrement the current month if the prev or next icon is clicked
        currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1
        
        if(currMonth < 0 || currMonth > 11) {
            // Update current month and year with newly created date month and year
            date = new Date(currYear, currMonth)
            currYear = date.getFullYear()
            currMonth = date.getMonth()
        } else {
            date = new Date() // pass the current date as date value
        }
        renderCalendar()
    })
})

// Open and close the booking time modal
let bookingTime_modal = document.getElementById("booking-time-modal")
function openBookingTimeModal(){
    bookingTime_modal.classList.add("open-booking-time-modal")
}
function closeBookingTimeModal(){
    bookingTime_modal.classList.remove("open-booking-time-modal")
}

// Open and close the booking form modal
let booking_modal = document.getElementById("booking-modal")
function openBookingModal(){
    booking_modal.classList.add("open-booking-modal")
}
function closeBookingModal(){
    booking_modal.classList.remove("open-booking-modal")
}

//chatgpt//
// Open booking form when a time is clicked
$('.time-block').click(function() {
    var timeClicked = this.className
    console.log("->" + timeClicked)
    
    closeBookingTimeModal()
    openBookingModal()
})
// Update your JavaScript to set the selected date and time in the hidden fields
$('.time-block').click(function() {
    var timeClicked = this.textContent;  // Get the clicked time slot
    var dateClicked = $('.current-date').text();  // Get the current date

    // Set the selected date and time in the hidden fields
    $('#booking-date').val(dateClicked);
    $('#booking-time').val(timeClicked);

    closeBookingTimeModal();
    openBookingModal();
});

// Update your JavaScript to submit the form when the Submit button is clicked
$('#booking-submit-button').click(function() {
    // Your form submission logic
});

$(function()
{
    $(".datepicker").datepicker();
});