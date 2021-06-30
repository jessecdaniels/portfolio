const daysofweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const dayindex = (new Date()).getDay();
const day = daysofweek[dayindex];

document.querySelector("header p").textContent=`Happy ${day}!`;

// ----------------------------------------------------------------
// Spotify API 
// ----------------------------------------------------------------

const songDiv = document.querySelector(".figure .song p");

document.addEventListener("DOMContentLoaded", getSong);

async function getSong() {
    const songData = await fetch("https://api.spotify.com/v1/me/player/currently-playing", {
        headers: {
            Accept: "application/json"
        }
    });
    const songObj = await songData.json();
    songDiv.innerHTML = songObj.joke;
    console.log(songData);
}