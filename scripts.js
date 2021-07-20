// ----------------------------------------------------------------
// Daily Greeting In Header (Array)
// ----------------------------------------------------------------

const daysofweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const dayindex = (new Date()).getDay();
const day = daysofweek[dayindex];

document.querySelector("header p").textContent=`Happy ${day}!`;


// ----------------------------------------------------------------
// Photography Slideshow
// ----------------------------------------------------------------

let currentSlide = 0;
const slides = document.querySelectorAll(".slide")
const dots = document.querySelectorAll('.dot')

const init = (n) => {
  slides.forEach((slide, index) => {
    slide.style.display = "none"
    dots.forEach((dot, index) => {
      dot.classList.remove("active")
    })
  })
  slides[n].style.display = "block"
  dots[n].classList.add("active")
}
document.addEventListener("DOMContentLoaded", init(currentSlide))
const next = () => {
  currentSlide >= slides.length - 1 ? currentSlide = 0 : currentSlide++
  init(currentSlide)
}

const prev = () => {
  currentSlide <= 0 ? currentSlide = slides.length - 1 : currentSlide--
  init(currentSlide)
}

document.querySelector(".next").addEventListener('click', next)

document.querySelector(".prev").addEventListener('click', prev)


setInterval(() => {
  next()
}, 5000);

dots.forEach((dot, i) => {
  dot.addEventListener("click", () => {
    console.log(currentSlide)
    init(i)
    currentSlide = i
  })
})


// -----------------------------------------------------------------------------------
// Spotify API | My Last Played Song
// going to come back to working on this when Spotify decides to play nicer with devs
// -----------------------------------------------------------------------------------

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



// ----------------------------------------------------------------
// Horoscope Feature (API Call)
// ----------------------------------------------------------------


const horoscopeDiv = document.querySelector(".info-box .horoscope p");

// document.addEventListener("DOMContentLoaded", getHoroscope); 
// used this to auto load horoscope before I added the select option

document.querySelector("#list").addEventListener("change", getHoroscope);

async function getHoroscope() {
  const sunsign = document.querySelector("#list").value;
    const horoscopeData = await fetch(`http://sandipbgt.com/theastrologer/api/horoscope/${sunsign}/today/`, {
        headers: {
            Accept: "application/json"
        }
    });
    const horoscopeObj = await horoscopeData.json();
    horoscopeDiv.innerHTML = horoscopeObj.horoscope;
    console.log(horoscopeObj);
}

// ----------------------------------------------------------------
// Word Count: Count and return the number of words in my bio
// ----------------------------------------------------------------

var wordsInPost = wordCount(document.querySelectorAll(".bio"));

function wordCount(words) {
	var count = 0;
	for (var i = 0; i < words.length; i++) {
		count += words[i].textContent.split(' ').length;
    count =`<h2>You may be interested to know this bio contains ${count} words</h2>`;
    document.querySelector("#wordcount").innerHTML = count;

	}
	return count;
}