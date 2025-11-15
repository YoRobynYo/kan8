console.log('Script loaded');


const menuButtons = document.querySelectorAll('.menu-btn');
const courseContent = document.getElementById('course-content');

console.log('menuButtons:', menuButtons);
console.log('courseContent:', courseContent);
console.log('Number of menu buttons found:', menuButtons.length);

const lessonsData = {
  "lesson-cover": "<h2>Cover Page</h2><p>Welcome to the course!</p>",
  "lesson-roadmap": "<h2>Roadmap</h2><p>This is where the journey begins.</p>",
  "lesson-variables": "<h2>Variables 📦</h2><p>Variables store information...</p>",
  "lesson-loops": "<h2>Loops 🔁</h2><p>Loops help you repeat tasks...</p>",
  "lesson-functions": "<h2>Functions 🧩</h2><p>Functions are reusable stations...</p>",
  "lesson-conditionals": "<h2>Conditionals ❓</h2><p>Conditionals make decisions...</p>",
  "lesson-operators": "<h2>Operators ⚡</h2><p>Operators do math and comparisons...</p>",
  "lesson-events": "<h2>Events ⚡</h2><p>Events listen to user actions...</p>"
};

function loadLesson(id) {
  courseContent.innerHTML = lessonsData[id] || "<p>Lesson not found.</p>";

}

menuButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const target = btn.getAttribute('data-target');
    loadLesson(target);
  });
});

// Load first lesson by default
loadLesson("lesson-cover");