const daysofweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const dayindex = (new Date()).getDay();
const day = daysofweek[dayindex];

document.querySelector("header p").textContent=`Happy ${day}!`;




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

const slides = document.querySelectorAll(".slide");
const nextBtn = document.querySelector(".nextBtn");
const prevBtn = document.querySelector(".prevBtn");
slides.forEach(function (slide, index) {
  slide.style.left = `${index * 100}%`;
});
let counter = 0;
nextBtn.addEventListener("click", function () {
  counter++;
  carousel();
});

prevBtn.addEventListener("click", function () {
  counter--;
  carousel();
});

function carousel() {
  // working with slides
  // if (counter === slides.length) {
  //   counter = 0;
  // }
  // if (counter < 0) {
  //   counter = slides.length - 1;
  // }
  // working with buttons

  if (counter < slides.length - 1) {
    nextBtn.style.display = "block";
  } else {
    nextBtn.style.display = "none";
  }
  if (counter > 0) {
    prevBtn.style.display = "block";
  } else {
    prevBtn.style.display = "none";
  }
  slides.forEach(function (slide) {
    slide.style.transform = `translateX(-${counter * 100}%)`;
  });
}

prevBtn.style.display = "none";



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