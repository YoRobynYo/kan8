==================================
==================================
==================================
==== new style for everything ====
==================================
==================================

To build this pdf we have made all the Fundamentals the same style and manner throughout this course.


==================================
  Variables 📦
==================================

Variables 📦

Variables are like boxes that store information. You can put numbers, words, or true/false answers inside them and use them later in your program.
Examples

We can make simple boxes using let. There is also const and var in JavaScript:

    let – creates a box you can change later.
    const – creates a box that cannot change after you set it.
    var – an old way to make a variable. It is no longer used because it has confusing rules for scope, so we only use let and const now.

let score = 10; // stores a number
const playerName = 'Alex'; // stores a name that doesn’t change

We can also store yes/no answers using true or false:
let hasKey = true;
let isDoorOpen = false;
💡 Helpful Explanation:

The + sign joins text and variables together. So 'Age: ' + age means “write the words 'Age: ' and then add what is stored in the variable age”. This is called string concatenation.

To make a message using our boxes, we can combine them like this:
let message = playerName + ' has ' + score + ' points';
console.log(message);
Step-by-Step Guide

1️⃣ Create a variable using let or const.
2️⃣ Choose what to store: a number, text in quotes, or a true/false value.
3️⃣ Give the variable a name that makes sense.
4️⃣ Use + to join text and numbers together.
5️⃣ Use console.log() to see what’s inside your box.
🧩 Mix It Up Practice Exercises
let age = 7;
let favoriteToy = 'teddy bear';
console.log('Age: ' + age + ', Toy: ' + favoriteToy);
let score = 15;
let player = 'Sam';
console.log(player + ' scored ' + score + ' points');
const hasKey = false;
let isDoorOpen = true;
console.log('Key: ' + hasKey + ', Door open: ' + isDoorOpen);
🔥 MegaMix Challenge

Use at least three variables in one message to create a story or scenario!
💡 Helpful Reminders:

    Variables are boxes: store numbers, words, or true/false values.
    Use let to create a variable you may change, or const for something fixed.
    var is no longer used because it has confusing scope rules; always use let or const.
    Names help you remember what’s inside the box.
    Use + to combine text and variables. This is called string concatenation.
    Check the output with console.log().

MegaMix 1
let player = 'Liam';
let score = 20;
let level = 1;
console.log(player + ' reached level ' + level + ' with ' + score + ' points');
MegaMix 2
let toy = 'robot';
let color = 'red';
let quantity = 3;
console.log('I have ' + quantity + ' ' + color + ' ' + toy + 's');
MegaMix 3
let name = 'Emma';
let pet = 'cat';
let food = 'fish';
console.log(name + ' feeds her ' + pet + ' some ' + food);
MegaMix 4
let city = 'Paris';
let weather = 'sunny';
let temperature = 22;
console.log('In ' + city + ', it is ' + weather + ' and ' + temperature + '°C');
MegaMix 5
let player1 = 'Mia';
let player2 = 'Noah';
let game = 'chess';
console.log(player1 + ' and ' + player2 + ' are playing ' + game);

Well done! You have completed the MegaMix variables 🎉


==================================
  Loops 🔁
==================================
  
Loops 🔁

Loops let us repeat actions multiple times without rewriting the code. It’s like pressing the play button again and again until the task is done!

Before we write the code, let’s understand what each part does. We want to count numbers from 1 to 5:

    for – tells the computer we are starting a loop.
    let i = 1; – makes a counter starting at 1.
    i <= 5; – keeps the loop running while i is 5 or less.
    i++ – increases i by 1 each time the loop runs.
    { } – everything inside these curly brackets is repeated each time.

for (let i = 1; i <= 5; i++) { console.log(i); // prints the current number }

Here, we count from 1 to 5. The code inside { } runs every time the number increases.
What is an Array?

Before we use an array, it helps to know: in another lesson we will go through arrays in deeper ways with further examples.

An array is a special box that can hold multiple items together. For example:
let pets = ['cat', 'dog'];

This means we have a box called pets that stores two things: 'cat' and 'dog'. We can use a loop to look at each item inside the array.
for (let i = 0; i < pets.length; i++) { console.log('Feed ' + pets[i]); // prints each pet in the list }

We go through each item in the array and print a message for it.
Step-by-Step Guide

1️⃣ Start with for and create a counter: let i = 0;
2️⃣ Set the condition: i < number of times or length of array;
3️⃣ Increase the counter each loop: i++
4️⃣ Write the code to repeat inside { }
5️⃣ Check the output to see your repeated actions!
🧩 Mix It Up Practice Exercises
for (let i = 1; i <= 3; i++) { console.log('Jump ' + i + ' times'); }
let pets = ['cat', 'dog']; for (let i = 0; i < pets.length; i++) { console.log('Feed ' + pets[i]); }
for (let i = 5; i > 0; i--) { console.log('Countdown: ' + i); }
🔥 MegaMix Challenge

Combine multiple loops or loop with arrays to see different outcomes.
💡 Helpful Reminders:

    for repeats actions for a set number of times.
    Use let i = 0 to start counting.
    i++ increases the counter each time.
    Inside { }, write the code that repeats.
    Arrays hold multiple items together and can be looped through.
    💡 Check output to ensure your loop works as expected.

MegaMix 1
for (let i = 1; i <= 4; i++) { console.log('Draw star ' + i); }
MegaMix 2
let fruits = ['apple', 'banana', 'cherry']; for (let i = 0; i < fruits.length; i++) { console.log('Eat ' + fruits[i]); }
MegaMix 3
for (let i = 10; i > 5; i--) { console.log('Count down: ' + i); }
MegaMix 4
let toys = ['car', 'doll', 'ball']; for (let i = 0; i < toys.length; i++) { console.log('Play with ' + toys[i]); }
MegaMix 5
for (let i = 1; i <= 3; i++) { for (let j = 1; j <= 2; j++) { console.log('Round ' + i + ', Step ' + j); } }

Well done! You have completed the MegaMix loops 🎉


==================================
  Functions 🔧
==================================

Functions are like small machines in your program. You give them instructions once, and they can do the same task again and again whenever you call them!

Imagine a popcorn machine — you press the button, and it pops popcorn every time. A function is like that button: once it’s made, you just use it when you need it.
Function Illustration

(Illustration goes here)
Examples
function makePopcorn() { console.log('🍿 Pop! Pop! Pop! The popcorn is ready!'); } makePopcorn();

This function makes popcorn! When you call makePopcorn(), it prints the message. You can use it as many times as you like without rewriting the code.
function greet(name) { console.log('Hello ' + name + '! Welcome back!'); } greet('Ava'); greet('Leo');

Here, the greet() function takes a name inside the brackets. When you call it with a name, it says hello to that person! These are called parameters — little boxes that hold information the function can use.
🧩 Mix It Up Practice Exercises

Try these small challenges — see if you can guess what each one will print before you run it!
Exercise 1
function feedPet() { console.log('Your pet is happy and full!'); } feedPet();
Exercise 2
function cookBreakfast() { console.log('Eggs are ready!'); } cookBreakfast();
Exercise 3
function startRace() { console.log('3...2...1... Go!'); } startRace();
Exercise 4
function makeSandwich(ingredient) { console.log('Here’s your ' + ingredient + ' sandwich!'); } makeSandwich('ham');
Exercise 5
function cheer(name) { console.log('Go ' + name + '!'); } cheer('Alex');
🔥 MegaMix Challenge

Now try combining functions with parameters, calling them multiple times, and printing different messages. They’ll test your understanding in a creative way.
💡 Helpful Reminders:

    Use function to define a function.
    Give your function a name that tells what it does.
    Put code inside { } to run when the function is called.
    Use parameters () if you want to pass information.
    Call your function by writing its name followed by ().

MegaMix 1
function greetPlayer(name) { console.log('Welcome, ' + name + '!'); } greetPlayer('Mia'); greetPlayer('Leo');
MegaMix 2
function addPoints(points) { console.log('You earned ' + points + ' points!'); } addPoints(5); addPoints(10);
MegaMix 3
function checkPetStatus(pet, status) { console.log(pet + ' is ' + status + '!'); } checkPetStatus('Dog', 'happy'); checkPetStatus('Cat', 'sleepy');
MegaMix 4
function countdown(number) { console.log(number + '...'); } countdown(3); countdown(2); countdown(1);
MegaMix 5
function celebrate(event) { console.log('Hooray! ' + event + ' is happening!'); } celebrate('Birthday'); celebrate('Victory');
MegaMix 6
function paint(color) { console.log('Painting the wall ' + color + '!'); } paint('blue'); paint('green');
MegaMix 7
function scoreGoal(player, points) { console.log(player + ' scored ' + points + ' points!'); } scoreGoal('Alex', 3); scoreGoal('Sam', 2);
MegaMix 8
function setAlarm(time) { console.log('Alarm is set for ' + time); } setAlarm('7:00 AM'); setAlarm('8:30 AM');
MegaMix 9
function throwParty(name, guests) { console.log('Party for ' + name + ' with ' + guests + ' guests!'); } throwParty('Mia', 5); throwParty('Leo', 10);
MegaMix 10
function runRace(player, laps) { console.log(player + ' runs ' + laps + ' laps!'); } runRace('Charlie', 3); runRace('Ella', 5);

Well done! You have completed the MegaMix functions 🎉


==================================
  Conditionals ❓
==================================

Conditionals let us ask questions and decide what our program should do based on the answer. It's like asking: "Is it raining?" If yes, do one thing; if no, do another.
Conditional Illustration

(Illustration goes here)
Examples
let isRaining = true; if (isRaining) { console.log('Take your umbrella!'); } else { console.log('No umbrella needed!'); }

This code checks if it’s raining. If it is, it prints a message to take an umbrella. Otherwise, it says no umbrella is needed.
let score = 10; if (score >= 10) { console.log('You win!'); } else { console.log('Try again!'); }

Here, we check if score is 10 or more. If it is, we win! Otherwise, we try again.
Step-by-Step Guide

1️⃣ Start with if and write your condition inside ( ).
2️⃣ Put { } around the code to run if the condition is true.
3️⃣ Optionally add else with { } for what happens if it’s false.
4️⃣ Check the output to see what your program does!
🧩 Mix It Up Practice Exercises
let isDoorOpen = false; if (isDoorOpen) { console.log('Walk through the door'); } else { console.log('Knock first!'); }
let hasKey = true; if (hasKey) { console.log('You can open the treasure chest!'); } else { console.log('Find a key first.'); }
let age = 12; if (age >= 13) { console.log('You can join the club!'); } else { console.log('Sorry, not old enough.'); }
🔥 MegaMix Challenge

Combine multiple conditionals! Ask more than one question in your code to see different outcomes.
💡 Helpful Reminders:

    if checks a condition.
    else runs code if the condition is not true.
    Use == or === to compare values.
    Use >, <, >=, <= for number comparisons.
    💡 Try thinking about the question first: What do I want to happen if true? What if false?
    💡 Break down each part: condition inside (), actions inside { }.
    💡 Check your output often to make sure your logic works.

MegaMix 1
let weather = 'rainy'; if (weather === 'rainy') { console.log('Take an umbrella'); } else { console.log('No umbrella needed'); }
MegaMix 2
let score = 15; if (score >= 10) { console.log('Level Up!'); } else { console.log('Keep trying'); }
MegaMix 3
let hasTicket = true; if (hasTicket) { console.log('Enter the cinema'); } else { console.log('Buy a ticket first'); }
MegaMix 4
let isHungry = false; if (isHungry) { console.log('Eat something'); } else { console.log('You are full'); }
MegaMix 5
let day = 'Saturday'; if (day === 'Saturday' || day === 'Sunday') { console.log('Time to play!'); } else { console.log('Go to school'); }

Well done! You have completed the MegaMix conditionals 🎉


==================================
  Operators ⚡
==================================

Operators are tools that let us work with the boxes (variables) we’ve made. They help us do things like add, subtract, combine, and compare values!
Operator Illustration

(Illustration goes here)
Examples
let score = 10; let bonus = 5; let total = score + bonus; console.log(total); // prints 15

This uses the + operator to combine numbers.
let playerName = 'Ava'; let message = playerName + ' has ' + score + ' points'; console.log(message);

Here + joins text and numbers to make a message.
Step-by-Step Guide

1️⃣ To use an operator, pick the box (variable) you want to work with.
2️⃣ Choose the action: add (+), subtract (-), multiply (*), divide (/), or compare (==, ===, <, >, >=, <=).
3️⃣ Write it between the boxes or values.
4️⃣ See the result in the output!
🧩 Mix It Up Practice Exercises
let apples = 3; let oranges = 2; console.log(apples + oranges); // prints 5
let score = 7; let bonus = 3; console.log(score * bonus); // prints 21
let player1 = 'Leo'; let player2 = 'Mia'; console.log(player1 + ' & ' + player2); // prints 'Leo & Mia'
🔥 MegaMix Challenge

Try combining different operators in one line! Can you add numbers and make a sentence with text? 🧠
💡 Helpful Reminders:

    Use + to add numbers or join text.
    Use -, *, / to do math with numbers.
    Use == or === to check if things are the same.
    Use >, <, >=, <= to compare numbers.

MegaMix 1
let a = 5; let b = 3; console.log(a + b);
MegaMix 2
let x = 10; let y = 2; console.log(x / y);
MegaMix 3
let name = 'Ava'; let points = 8; console.log(name + ' has ' + points + ' points');
MegaMix 4
let score = 12; console.log(score >= 10); // true
MegaMix 5
let apples = 4; let oranges = 5; console.log(apples == oranges); // false

Well done! You have completed the MegaMix operators 🎉








what makes this work ::

Looking at the Kan8 Fundamentals sequence we’ve been building, the next sections after Functions are likely:

    Events – handling things like clicks, mouse movements, and other actions.

    Arrays – storing multiple items in one variable (“boxes that can hold many things”).

    Objects – named collections of properties, like a backpack with labeled compartments.

We’ve already done Variables, Loops, Conditionals, Operators, and Functions. The logical next one is Events, and we can continue using the same child-friendly layout:

    Explanation of the concept

    Illustration placeholder

    Simple examples broken down step by step

    Step-by-step guide with a “formula”

    Mix It Up Exercises

    MegaMix Challenge

    Helpful reminders and small tips

