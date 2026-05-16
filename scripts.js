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
// Deterministic daily generator: sign + date produces a consistent
// reading for the day without depending on any external API.
// ----------------------------------------------------------------
const horoscopeSelect = document.getElementById('list');
const horoscopeResult = document.querySelector('.horoscope-result');

const horoscopePool = [
  "Today calls for patience. The answers you're looking for are closer than they appear — give them room to arrive.",
  "A creative idea you've been sitting on is worth revisiting. The timing that felt off before may finally be right.",
  "Someone in your orbit is paying closer attention than you think. Show up as your full self today.",
  "Resist the urge to over-explain. Your instincts are solid. Trust them and move.",
  "An unexpected conversation could shift your perspective on something you thought was settled.",
  "Energy is high today. Channel it into the work that actually matters rather than what feels urgent.",
  "The thing you've been putting off will feel lighter than you expect once you start. Just start.",
  "Pay attention to what drains you and what refills you today. That contrast is telling you something.",
  "A small gesture of generosity comes back around in ways you won't anticipate. Give freely.",
  "Today is better spent listening than talking. You'll learn something worth knowing.",
  "Clarity is coming, but not on your timeline. Sit with the uncertainty a little longer.",
  "The right door won't require you to force it. If something feels like a battle, look for the other door.",
  "Your attention is your most valuable resource today. Guard it like you mean it.",
  "Something you built or said weeks ago is paying off right now, even if quietly.",
  "Bold moves are favored today. The version of you who hesitates is not the version needed right now.",
  "Rest is not the same as giving up. Recharging is part of the work.",
  "A pattern you keep repeating is asking to be examined. You already know which one.",
  "Today's small decisions are building something larger. Choose accordingly.",
  "The most interesting path forward is probably the one you haven't considered yet.",
  "Lead with curiosity today rather than certainty. You'll get further."
];

function dailySeed(sign) {
  const today = new Date();
  const dateStr = `${today.getFullYear()}${today.getMonth()}${today.getDate()}`;
  const combined = sign + dateStr;
  let hash = 0;
  for (let i = 0; i < combined.length; i++) {
    hash = (hash * 31 + combined.charCodeAt(i)) & 0xffffffff;
  }
  return Math.abs(hash) % horoscopePool.length;
}

if (horoscopeSelect && horoscopeResult) {
  horoscopeSelect.addEventListener('change', () => {
    const sign = horoscopeSelect.value;
    horoscopeResult.textContent = horoscopePool[dailySeed(sign)];
  });
}
