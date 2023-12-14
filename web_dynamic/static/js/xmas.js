//updateCountdown function
function updateCountdown() {
  const christmasDate = new Date('December 25, 2023 00:00:00').getTime();
  const currentDate = new Date().getTime();
  const timeDifference = christmasDate - currentDate;

  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  document.getElementById('days').innerText = formatTime(days);
  document.getElementById('hours').innerText = formatTime(hours);
  document.getElementById('minutes').innerText = formatTime(minutes);
  document.getElementById('seconds').innerText = formatTime(seconds);
}

function formatTime(time) {
  return time < 10 ? `0${time}` : time;
}

//Update each digit
function updateDigit(digitId, newValue) {
  const digitElement = document.getElementById(digitId);
  const currentDigit = digitElement.innerText;

  if (currentDigit !== newValue) {
    digitElement.classList.add('changing');
    setTimeout(() => {
      digitElement.innerText = newValue;
      digitElement.classList.remove('changing');
    }, 500);
  }
}
// Update the countdown every second
setInterval(updateCountdown, 1000);

// Initial update
updateCountdown();
