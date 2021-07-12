const daysofweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const dayindex = (new Date()).getDay();
const day = daysofweek[dayindex];

document.querySelector("header p").textContent=`Happy ${day}!`;


// ----------------------------------------------------------------
// Horoscope Feature
// ----------------------------------------------------------------

const button = document.querySelector(".info-box button");
const horoscopeDiv = document.querySelector(".info-box .horoscope p");

// document.addEventListener("DOMContentLoaded", getHoroscope);

button.addEventListener("click", getHoroscope);

async function getHoroscope() {
    const horoscopeData = await fetch("http://sandipbgt.com/theastrologer/api/horoscope/cancer/today/", {
        headers: {
            Accept: "application/json"
        }
    });
    const horoscopeObj = await horoscopeData.json();
    horoscopeDiv.innerHTML = horoscopeObj.horoscope;
    console.log(horoscopeData);
}

// ----------------------------------------------------------------
// Photography Slideshow
// ----------------------------------------------------------------

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}


// ----------------------------------------------------------------
// Spotify API | My Last Played Song
// ----------------------------------------------------------------

// const songDiv = document.querySelector(".figure .song p");

// document.addEventListener("DOMContentLoaded", getSong);

// async function getSong() {
//     const songData = await fetch("https://api.spotify.com/v1/me/player/recently-played?limit=1", {
//         headers: {
//             Accept: "application/json"
//         }
//     });
//     const songObj = await songData.json();
//     songDiv.innerHTML = songObj.song;
//     console.log(songData);

// 