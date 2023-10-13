const daysTag = document.querySelector(".days"),
  currentDate = document.querySelector(".current-date"),
  prevNextIcon = document.querySelectorAll(".icons span");

let date = new Date(),
  currYear = date.getFullYear(),
  currMonth = date.getMonth();

const months = [
  "January", "February", "March", "April", "May", "June", "July",
  "August", "September", "October", "November", "December"
];

const renderCalendar = () => {
  let firstDayofMonth = new Date(currYear, currMonth, 1).getDay(),
    lastDateofMonth = new Date(currYear, currMonth + 1, 0).getDate(),
    lastDayofMonth = new Date(currYear, currMonth, lastDateofMonth).getDay(),
    lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate();
  let liTag = "";

  for (let i = firstDayofMonth; i > 0; i--) {
    liTag += `<li class="inactive">${lastDateofLastMonth - i + 1}</li>`;
  }

  for (let i = 1; i <= lastDateofMonth; i++) {
    let isToday = i === date.getDate() && currMonth === date.getMonth() && currYear === date.getFullYear() ? "active" : "";
    liTag += `<li class="${isToday}" onclick="selectDate(${i})">${i}</li>`;
  }

  for (let i = lastDayofMonth; i < 6; i++) {
    liTag += `<li class="inactive">${i - lastDayofMonth + 1}</li>`;
  }

  currentDate.innerText = `${months[currMonth]} ${currYear}`;
  daysTag.innerHTML = liTag;
};

const selectDate = (day) => {
    const selectedDate = new Date(currYear, currMonth, day);
    const dayOfMonth = selectedDate.getDate();
    const month = selectedDate.toLocaleString('default', { month: 'long' });
    const year = selectedDate.getFullYear();
    const formattedDate = `${dayOfMonth} ${month} ${year}`;
    document.getElementById('booking-date').value = formattedDate;
    openBookingTimeModal();
};


renderCalendar();

prevNextIcon.forEach(icon => {
  icon.addEventListener("click", () => {
    currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;

    if (currMonth < 0 || currMonth > 11) {
      date = new Date(currYear, currMonth);
      currYear = date.getFullYear();
      currMonth = date.getMonth();
    } else {
      date = new Date();
    }
    renderCalendar();
  });
});

let bookingTime_modal = document.getElementById("booking-time-modal");

function openBookingTimeModal() {
  bookingTime_modal.classList.add("open-booking-time-modal");
}

function closeBookingTimeModal() {
  bookingTime_modal.classList.remove("open-booking-time-modal");
}

let booking_modal = document.getElementById("booking-modal");

function openBookingModal() {
  booking_modal.classList.add("open-booking-modal");
}

function closeBookingModal() {
  booking_modal.classList.remove("open-booking-modal");
}
// Add a new function to handle time selection
const selectTime = (time) => {
    document.getElementById('booking-time').value = time;
    closeBookingTimeModal();
    openBookingModal();
};
document.querySelectorAll('.time-block').forEach(timeBlock => {
    timeBlock.addEventListener('click', () => {
        const selectedTime = timeBlock.getAttribute('data-time');
        selectTime(selectedTime);
    });
});

