// ----------------------------------------------------------------
// Daily Greeting in Hero
// ----------------------------------------------------------------
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const day = days[new Date().getDay()];
const greetingEl = document.getElementById('greeting');
if (greetingEl) greetingEl.textContent = `Happy ${day}!`;


// ----------------------------------------------------------------
// Mobile Nav Toggle
// ----------------------------------------------------------------
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => navLinks.classList.remove('open'));
  });
}


// ----------------------------------------------------------------
// Photography Slideshow
// ----------------------------------------------------------------
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');

function showSlide(n) {
  slides.forEach(s => s.style.display = 'none');
  dots.forEach(d => d.classList.remove('active'));
  if (slides[n]) slides[n].style.display = 'block';
  if (dots[n]) dots[n].classList.add('active');
}

document.addEventListener('DOMContentLoaded', () => showSlide(currentSlide));

function nextSlide() {
  currentSlide = currentSlide >= slides.length - 1 ? 0 : currentSlide + 1;
  showSlide(currentSlide);
}

function prevSlide() {
  currentSlide = currentSlide <= 0 ? slides.length - 1 : currentSlide - 1;
  showSlide(currentSlide);
}

const nextBtn = document.querySelector('.next');
const prevBtn = document.querySelector('.prev');
if (nextBtn) nextBtn.addEventListener('click', nextSlide);
if (prevBtn) prevBtn.addEventListener('click', prevSlide);

setInterval(nextSlide, 5000);

dots.forEach((dot, i) => {
  dot.addEventListener('click', () => {
    currentSlide = i;
    showSlide(currentSlide);
  });
});


// ----------------------------------------------------------------
// Word Count on Bio
// ----------------------------------------------------------------
const bioEl = document.querySelector('.bio');
const wordcountEl = document.getElementById('wordcount');

if (bioEl && wordcountEl) {
  const text = bioEl.textContent || '';
  const count = text.trim().split(/\s+/).filter(w => w.length > 0).length;
  wordcountEl.textContent = `** Fun fact: this bio contains ${count} words, according to my JavaScript word counter **`;
}


// ----------------------------------------------------------------
// Horoscope Feature
// Uses horoscope-app-api.vercel.app (free, no key required)
// ----------------------------------------------------------------
const horoscopeSelect = document.getElementById('list');
const horoscopeResult = document.querySelector('.horoscope-result');

if (horoscopeSelect && horoscopeResult) {
  horoscopeSelect.addEventListener('change', getHoroscope);
}

async function getHoroscope() {
  const sign = horoscopeSelect.value;
  horoscopeResult.textContent = 'Reading the stars...';

  try {
    const res = await fetch(
      `https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=${sign}&day=today`
    );
    if (!res.ok) throw new Error('API error');
    const data = await res.json();
    horoscopeResult.textContent = data?.data?.horoscope_data || 'The stars are quiet today. Try again later.';
  } catch {
    horoscopeResult.textContent = 'Could not load horoscope right now. The cosmos are mysterious like that.';
  }
}
