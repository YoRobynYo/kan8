<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Full PDF Mockup</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #2c3e50;
            padding: 20px;
        }
        
        .controls {
            max-width: 800px;
            margin: 0 auto 20px;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        
        .controls h2 {
            color: #667eea;
            margin-bottom: 15px;
        }
        
        .button-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 15px;
        }
        
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
        }
        
        button:hover {
            background: #764ba2;
            transform: translateY(-2px);
        }
        
        button.active {
            background: #4facfe;
        }
        
        .page-counter {
            text-align: center;
            font-size: 18px;
            color: #333;
            font-weight: bold;
        }
        
        /* A4 Page styling */
        .page {
            width: 210mm;
            min-height: 297mm;
            background: white;
            margin: 0 auto 20px;
            padding: 20mm;
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            position: relative;
            page-break-after: always;
        }
        
        .page-number {
            position: absolute;
            bottom: 10mm;
            right: 20mm;
            color: #999;
            font-size: 12px;
        }
        
        .page-header {
            border-bottom: 3px solid #667eea;
            padding-bottom: 5mm;
            margin-bottom: 10mm;
        }
        
        .page-title {
            font-size: 28px;
            color: #667eea;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .page-subtitle {
            font-size: 14px;
            color: #666;
        }
        
        .content-section {
            margin-bottom: 8mm;
        }
        
        .content-section h3 {
            color: #4facfe;
            font-size: 20px;
            margin-bottom: 5mm;
        }
        
        .content-section p {
            line-height: 1.6;
            margin-bottom: 4mm;
            text-align: justify;
        }
        
        .visual-placeholder {
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            border: 2px dashed #2196f3;
            border-radius: 8px;
            padding: 20mm;
            text-align: center;
            color: #1976d2;
            font-weight: bold;
            margin: 5mm 0;
        }
        
        .two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10mm;
            margin: 5mm 0;
        }
        
        .box {
            background: #f8f9fa;
            border: 2px solid #667eea;
            border-radius: 5px;
            padding: 5mm;
        }
        
        .exercise-box {
            background: #fff3cd;
            border: 3px solid #ffc107;
            border-radius: 8px;
            padding: 5mm;
            margin: 5mm 0;
        }
        
        .exercise-box h4 {
            color: #f57c00;
            margin-bottom: 3mm;
        }
        
        .code-block {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 5mm;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            margin: 3mm 0;
            overflow-x: auto;
        }
        
        .demo-exercise {
            background: #e3f2fd;
            border-left: 5px solid #2196f3;
            padding: 5mm;
            margin: 5mm 0;
        }
        
        .practice-exercise {
            background: #f3e5f5;
            border-left: 5px solid #9c27b0;
            padding: 5mm;
            margin: 5mm 0;
        }
        
        .checkbox {
            display: inline-block;
            width: 15px;
            height: 15px;
            border: 2px solid #333;
            margin-right: 5px;
            vertical-align: middle;
        }
        
        .hint-box {
            background: #fff8e1;
            border: 2px dashed #ffa726;
            padding: 3mm;
            margin-top: 3mm;
            border-radius: 5px;
        }
        
        ul, ol {
            margin-left: 8mm;
            line-height: 1.8;
        }
        
        .formula-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 5mm;
            border-radius: 8px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin: 5mm 0;
        }
        
        .cover-page {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 40mm 20mm;
        }
        
        .cover-title {
            font-size: 42px;
            color: #667eea;
            font-weight: bold;
            margin-bottom: 10mm;
        }
        
        .cover-subtitle {
            font-size: 20px;
            color: #666;
            margin-bottom: 20mm;
        }
        
        .cover-visual {
            width: 80%;
            height: 100mm;
            margin: 10mm 0;
        }
        
        @media print {
            body {
                background: white;
            }
            .controls {
                display: none;
            }
            .page {
                margin: 0;
                box-shadow: none;
            }
        }
    </style>
</head>
<body>
    <div class="controls">
        <h2>📄 Full PDF Preview - Navigate Pages</h2>
        <div class="button-group">
            <button onclick="showSection('all')">Show All Pages</button>
            <button onclick="showSection('intro')">Introduction (1-6)</button>
            <button onclick="showSection('var')">Variables (7-20)</button>
            <button onclick="showSection('types')">Data Types (21-34)</button>
            <button onclick="showSection('sample')">Show Sample Pages Only</button>
        </div>
        <div class="page-counter" id="pageCounter">
            Showing sample pages (scroll to see more)
        </div>
    </div>

    <div id="pdfPages">
        
        <!-- PAGE 1: COVER -->
        <div class="page cover-page" data-section="intro">
            <div class="cover-title">CourseForChildren<br>Kan8 Learning System</div>
            <div class="cover-subtitle">Let's Learn The Fundamentals of Programming<br>and Start Your Journey Today!</div>
            
            <!-- FUN ILLUSTRATION WITH SVG - 4 LEARNING STEPS -->
            <svg width="100%" height="200" viewBox="0 0 500 200" style="margin: 15mm 0;">
                <!-- STEP 1: TEACH - Graduation Cap / Headmaster Hat -->
                <g transform="translate(60, 80)">
                    <circle cx="0" cy="0" r="45" fill="#4facfe" stroke="#1976d2" stroke-width="3"/>
                    <!-- Mortarboard (graduation cap) -->
                    <rect x="-25" y="-35" width="50" height="8" fill="#1976d2" rx="2"/>
                    <rect x="-18" y="-27" width="36" height="20" fill="#2196f3"/>
                    <circle cx="25" cy="-35" r="3" fill="#ffc107"/>
                    <line x1="25" y1="-35" x2="32" y2="-45" stroke="#ffc107" stroke-width="2"/>
                    <text x="0" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#1976d2">TEACH</text>
                    <text x="0" y="48" text-anchor="middle" font-size="10" fill="#666">Learn it</text>
                </g>
                
                <!-- Arrow -->
                <path d="M 105 80 L 135 80" stroke="#333" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
                
                <!-- STEP 2: SHOW - Binoculars / Eye -->
                <g transform="translate(180, 80)">
                    <circle cx="0" cy="0" r="45" fill="#9c27b0" stroke="#6a1b9a" stroke-width="3"/>
                    <!-- Binoculars -->
                    <ellipse cx="-12" cy="-5" rx="12" ry="15" fill="#6a1b9a" stroke="#4a148c" stroke-width="2"/>
                    <ellipse cx="12" cy="-5" rx="12" ry="15" fill="#6a1b9a" stroke="#4a148c" stroke-width="2"/>
                    <rect x="-8" y="-10" width="16" height="4" fill="#6a1b9a"/>
                    <circle cx="-12" cy="-5" r="6" fill="#e1bee7"/>
                    <circle cx="12" cy="-5" r="6" fill="#e1bee7"/>
                    <circle cx="-12" cy="-5" r="3" fill="#4a148c"/>
                    <circle cx="12" cy="-5" r="3" fill="#4a148c"/>
                    <text x="0" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#6a1b9a">SHOW</text>
                    <text x="0" y="48" text-anchor="middle" font-size="10" fill="#666">Watch it</text>
                </g>
                
                <!-- Arrow -->
                <path d="M 225 80 L 255 80" stroke="#333" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
                
                <!-- STEP 3: PRACTICE - Pencil / Write -->
                <g transform="translate(300, 80)">
                    <circle cx="0" cy="0" r="45" fill="#4caf50" stroke="#2e7d32" stroke-width="3"/>
                    <!-- Pencil -->
                    <rect x="-4" y="-25" width="8" height="35" fill="#ffc107" stroke="#f57c00" stroke-width="2"/>
                    <polygon points="0,-28 -6,-35 6,-35" fill="#ff6f00"/>
                    <circle cx="0" cy="-38" r="2" fill="#333"/>
                    <rect x="-4" y="10" width="8" height="6" fill="#ff6f00"/>
                    <!-- Paper lines underneath -->
                    <line x1="-15" y1="15" x2="15" y2="15" stroke="#2e7d32" stroke-width="2"/>
                    <line x1="-15" y1="20" x2="12" y2="20" stroke="#2e7d32" stroke-width="2"/>
                    <text x="0" y="40" text-anchor="middle" font-size="14" font-weight="bold" fill="#2e7d32">PRACTICE</text>
                    <text x="0" y="53" text-anchor="middle" font-size="10" fill="#666">Try it</text>
                </g>
                
                <!-- Arrow -->
                <path d="M 345 80 L 375 80" stroke="#333" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
                
                <!-- STEP 4: REINFORCE - Light Bulb / Remember -->
                <g transform="translate(420, 80)">
                    <circle cx="0" cy="0" r="45" fill="#ffc107" stroke="#f57c00" stroke-width="3"/>
                    <!-- Light bulb -->
                    <circle cx="0" cy="-8" r="12" fill="#fff59d" stroke="#f57c00" stroke-width="2"/>
                    <rect x="-5" y="4" width="10" height="8" fill="#ffb74d" stroke="#f57c00" stroke-width="2" rx="1"/>
                    <line x1="-2" y1="12" x2="2" y2="12" stroke="#f57c00" stroke-width="2"/>
                    <line x1="-3" y1="15" x2="3" y2="15" stroke="#f57c00" stroke-width="2"/>
                    <!-- Light rays -->
                    <line x1="-18" y1="-8" x2="-22" y2="-8" stroke="#fff59d" stroke-width="2"/>
                    <line x1="18" y1="-8" x2="22" y2="-8" stroke="#fff59d" stroke-width="2"/>
                    <line x1="-13" y1="-18" x2="-16" y2="-21" stroke="#fff59d" stroke-width="2"/>
                    <line x1="13" y1="-18" x2="16" y2="-21" stroke="#fff59d" stroke-width="2"/>
                    <line x1="0" y1="-23" x2="0" y2="-27" stroke="#fff59d" stroke-width="2"/>
                    <text x="0" y="40" text-anchor="middle" font-size="13" font-weight="bold" fill="#f57c00">REMEMBER</text>
                    <text x="0" y="53" text-anchor="middle" font-size="10" fill="#666">Keep it</text>
                </g>
                
                <!-- Arrow definition -->
                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
                        <polygon points="0 0, 10 3, 0 6" fill="#333"/>
                    </marker>
                </defs>
                
                <!-- Fun stars decoration around the process -->
                <polygon points="30,20 33,28 42,28 35,33 37,42 30,36 23,42 25,33 18,28 27,28" fill="#ffeb3b" stroke="#f57c00" stroke-width="1"/>
                <polygon points="470,20 473,28 482,28 475,33 477,42 470,36 463,42 465,33 458,28 467,28" fill="#ffeb3b" stroke="#f57c00" stroke-width="1"/>
                <polygon points="250,160 253,168 262,168 255,173 257,182 250,176 243,182 245,173 238,168 247,168" fill="#4facfe" stroke="#1976d2" stroke-width="1"/>
            </svg>
            
            <div style="margin-top: 10mm; background: #f0f7ff; padding: 8mm; border-radius: 10px; border: 2px solid #4facfe;">
                <p style="font-size: 14px; color: #1976d2; margin: 0; text-align: center; line-height: 1.6;">
                    <strong>Every Fundamental Follows This Path:</strong><br>
                    Learn the Concept → Watch Examples → Practice Yourself → Remember Forever!
                </p>
            </div>
            
            <div style="margin-top: 10mm;">
                <p style="font-size: 16px; color: #666; font-weight: bold;">Authors: Robyn Mai / Bikya</p>
                <p style="font-size: 14px; color: #999; margin-top: 5mm;">Part 1 — Fundamentals (All 5)</p>
                <p style="font-size: 12px; color: #999;">A4 — Print & Digital</p>
            </div>
        </div>

        <!-- PAGE 2: WELCOME -->
        <div class="page" data-section="intro">
            <div class="page-header">
                <div class="page-title">Welcome / Project Overview</div>
            </div>
            
            <div class="content-section">
                <p>Welcome to your programming journey! This course will teach you the building blocks that every programmer needs to know. Think of it like learning to build with special blocks — once you understand how each block works, you can build anything you imagine.</p>
                
                <p>We're going to take this step by step. You'll learn one important idea at a time, practice it with exercises, and then move on to the next. By the end, you'll understand how real programs work and you'll be ready to create your own projects.</p>
            </div>
            
            <div class="two-column">
                <div>
                    <div class="visual-placeholder" style="height: 40mm;">
                        [DIAGRAM: Roadmap graphic<br>
                        Welcome → Fundamentals → Exercises → Progress → Sweet Factory]
                    </div>
                </div>
                <div>
                    <div class="box">
                        <h4 style="color: #667eea; margin-bottom: 3mm;">Key Ideas:</h4>
                        <ul>
                            <li>We'll learn one thing at a time — like building a machine out of cogs</li>
                            <li>You'll practice lots of little exercises, then put them together</li>
                            <li>Each fundamental builds on the last one</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="content-section">
                <p><em>This part focuses on Fundamentals 1–5. We'll start with Variables and work through all five fundamentals together.</em></p>
            </div>
            
            <div class="page-number">Page 2</div>
        </div>

        <!-- PAGE 3: WHY LEARN PROGRAMMING -->
        <div class="page" data-section="intro">
            <div class="page-header">
                <div class="page-title">Why Learn Programming</div>
            </div>
            
            <div class="two-column">
                <div class="content-section">
                    <h3>🧩 Problem-Solving</h3>
                    <p>Programming teaches you to break big problems into small steps. This helps you solve puzzles, fix things, and figure out how things work.</p>
                    
                    <h3>💡 Creativity</h3>
                    <p>You can build games, apps, art, music, and tools that help people. Programming turns your ideas into real things.</p>
                    
                    <h3>⚡ Make Things Happen</h3>
                    <p>Want a character to jump? A score to increase? A message to appear? Programming gives you the power to make it happen exactly how you want.</p>
                </div>
                
                <div>
                    <div class="visual-placeholder" style="height: 80mm;">
                        [FLOW DIAGRAM: Circular flow with cogs<br>
                        Idea → Steps → Build → Test → Improve<br>
                        Arrows showing continuous cycle]
                    </div>
                </div>
            </div>
            
            <div class="box" style="margin-top: 10mm; text-align: center; background: #667eea; color: white;">
                <p style="font-size: 16px; margin: 0;"><strong>Master these fundamentals and you'll be able to learn any programming language.</strong></p>
            </div>
            
            <div class="page-number">Page 3</div>
        </div>

        <!-- PAGE 4: FUNDAMENTALS OVERVIEW -->
        <div class="page" data-section="intro">
            <div class="page-header">
                <div class="page-title">Fundamentals Overview</div>
                <div class="page-subtitle">This Book — All 5 Fundamentals</div>
            </div>
            
            <div class="content-section">
                <p>This course covers five essential fundamentals that every programmer must know:</p>
                
                <ol style="line-height: 2; font-size: 16px;">
                    <li><strong>Variables / Data Storage</strong> — How programs remember things</li>
                    <li><strong>Data Types</strong> — Different kinds of information (numbers, words, true/false)</li>
                    <li><strong>Operators</strong> — How to do math, compare things, and make calculations</li>
                    <li><strong>Sequences / Order of Execution</strong> — Following steps in the correct order</li>
                    <li><strong>Conditionals (Decision Making)</strong> — Making programs choose different paths</li>
                </ol>
            </div>
            
            <div class="visual-placeholder" style="height: 60mm; margin: 8mm 0;">
                [DIAGRAM: Map showing 5 fundamentals as connected cogs<br>
                Each labeled with number and color:<br>
                1-Variables(Blue), 2-DataTypes(Teal), 3-Operators(Purple), 4-Sequences(Green), 5-Conditionals(Yellow)]
            </div>
            
            <div class="box">
                <h4 style="color: #667eea; margin-bottom: 3mm;">For each fundamental you will:</h4>
                <p style="margin: 0; font-size: 15px;"><strong>Learn</strong> → Understand the concept<br>
                <strong>See</strong> → Watch demonstrations (5 examples)<br>
                <strong>Try</strong> → Practice independently (10 exercises)<br>
                <strong>Check</strong> → Verify your work<br>
                <strong>Remember</strong> → Review the formula and recap</p>
            </div>
            
            <div class="page-number">Page 4</div>
        </div>

        <!-- PAGE 5: USING THE COURSE MENU -->
        <div class="page" data-section="intro">
            <div class="page-header">
                <div class="page-title">Using the Course Menu</div>
                <div class="page-subtitle">How to Navigate and Track Your Progress</div>
            </div>
            
            <div class="content-section">
                <p>Whether you're using this course digitally or with a printed workbook, here's how to get the most out of it:</p>
            </div>
            
            <div class="box" style="margin-bottom: 8mm;">
                <h4 style="color: #667eea; margin-bottom: 3mm;">📱 Digital Version:</h4>
                <ul>
                    <li><strong>Menu Navigation:</strong> Landing → Fundamentals → Exercises → Progress</li>
                    <li><strong>Kanban Board:</strong> Track your progress on micro-exercises for fundamentals 1–5</li>
                    <li><strong>Code Section:</strong> Write and run your code directly in the browser</li>
                </ul>
            </div>
            
            <div class="visual-placeholder" style="height: 70mm;">
                [DIAGRAM: Split screen showing<br>
                LEFT: Kanban board with cards for each fundamental<br>
                RIGHT: Code editor area with Run button<br>
                Arrows showing: Select exercise → Write code → Run → Check off]
            </div>
            
            <div class="box">
                <h4 style="color: #667eea; margin-bottom: 3mm;">📄 Print Version:</h4>
                <ul>
                    <li>Use the checkbox ☐ next to each exercise to track completion</li>
                    <li>Write your code/answers in the spaces provided</li>
                    <li>Check your work against the "Expected Result" section</li>
                </ul>
            </div>
            
            <div class="page-number">Page 5</div>
        </div>

        <!-- PAGE 6: SETTING UP FOR EXERCISES -->
        <div class="page" data-section="intro">
            <div class="page-header">
                <div class="page-title">Setting Up for Exercises</div>
                <div class="page-subtitle">Get Ready to Learn!</div>
            </div>
            
            <div class="content-section">
                <h3>Step-by-Step Setup:</h3>
                
                <div class="box" style="margin-bottom: 5mm;">
                    <p><strong>Step 1:</strong> Open your Kanban board (digital) or have this workbook ready (print)</p>
                </div>
                
                <div class="box" style="margin-bottom: 5mm;">
                    <p><strong>Step 2:</strong> Open your code editor (digital) or have a pencil ready (print)</p>
                </div>
                
                <div class="box" style="margin-bottom: 5mm;">
                    <p><strong>Step 3:</strong> Read each exercise carefully before starting</p>
                </div>
                
                <div class="box" style="margin-bottom: 5mm;">
                    <p><strong>Step 4:</strong> For demonstrations: Watch and follow along</p>
                </div>
                
                <div class="box">
                    <p><strong>Step 5:</strong> For practice: Try it yourself, then check your answer</p>
                </div>
            </div>
            
            <div class="visual-placeholder" style="height: 60mm; margin-top: 8mm;">
                [DIAGRAM: Flow chart showing the exercise process<br>
                Read Exercise → Watch Demo (if applicable) → Try It Yourself → Check Result → Mark Complete<br>
                Circular arrows showing: If stuck → Read Hint → Try Again]
            </div>
            
            <div class="box" style="margin-top: 8mm; background: #fff3cd;">
                <p style="margin: 0;"><strong>💡 Remember:</strong> It's okay to make mistakes! That's how we learn. If something doesn't work, read the hint and try again.</p>
            </div>
            
            <div class="page-number">Page 6</div>
        </div>

        <!-- PAGE 7: FUNDAMENTAL 1 - INTRO TO VARIABLES -->
        <div class="page" data-section="var">
            <div class="page-header" style="border-color: #4facfe;">
                <div class="page-title" style="color: #4facfe;">Fundamental 1: Variables / Data Storage</div>
                <div class="page-subtitle">How Programs Remember Things</div>
            </div>
            
            <div class="formula-box" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                Variable = Name + Value
            </div>
            
            <div class="content-section">
                <h3>What is a Variable?</h3>
                <p><strong>A variable is a labeled box your program uses to remember something.</strong></p>
                
                <p>Think about your toy box at home. You might have different boxes labeled "LEGO," "Action Figures," and "Art Supplies." When you want to find your LEGO, you know exactly which box to look in!</p>
                
                <p>Variables work the same way in programming. They're labeled containers that store information your program needs to remember.</p>
            </div>
            
            <div class="two-column" style="margin: 8mm 0;">
                <div class="visual-placeholder" style="height: 60mm;">
                    [ILLUSTRATION: Three labeled boxes<br>
                    Box 1: "color" → contains "blue"<br>
                    Box 2: "score" → contains 0<br>
                    Box 3: "playerName" → contains "Sam"<br>
                    Arrows showing put-in and read-out]
                </div>
                <div>
                    <div class="box">
                        <h4 style="color: #4facfe; margin-bottom: 3mm;">What Variables Can Hold:</h4>
                        <ul>
                            <li><strong>Numbers</strong> — scores, ages, amounts</li>
                            <li><strong>Text</strong> — names, colors, messages</li>
                            <li><strong>True/False</strong> — yes/no answers</li>
                        </ul>
                    </div>
                    <div class="box" style="margin-top: 5mm;">
                        <h4 style="color: #4facfe; margin-bottom: 3mm;">Where We Use Variables:</h4>
                        <ul>
                            <li>Keeping track of scores</li>
                            <li>Storing player names</li>
                            <li>Remembering chosen colors</li>
                            <li>Counting collected items</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="page-number">Page 7</div>
        </div>

        <!-- PAGE 8: HOW VARIABLES WORK -->
        <div class="page" data-section="var">
            <div class="page-header" style="border-color: #4facfe;">
                <div class="page-title" style="color: #4facfe;">How Variables Work — Step by Step</div>
            </div>
            
            <div class="visual-placeholder" style="height: 100mm; margin: 8mm 0;">
                [LARGE DIAGRAM: Three vertical sections showing the lifecycle<br><br>
                STAGE 1 - CREATE:<br>
                Empty box appears with label "score"<br>
                Caption: "First, we create a labeled box"<br><br>
                STAGE 2 - STORE:<br>
                Box now shows "0" inside<br>
                Arrow pointing into box<br>
                Caption: "Then we put a value into it"<br><br>
                STAGE 3 - USE/CHANGE:<br>
                Star icon → score = score + 1 → Box shows "1"<br>
                Caption: "We can read it and change it whenever we need"]
            </div>
            
            <div class="box">
                <h4 style="color: #4facfe; margin-bottom: 3mm;">Why This Matters:</h4>
                <p>Programs need to remember things while they run. Imagine a game that forgot your score every second — it wouldn't work! Variables are how programs store information so they can remember and react later.</p>
                
                <p style="margin-top: 4mm;">When you collect a star, the program adds 1 to your score. When you finish the level, it can show you the final score. All of this works because of variables.</p>
            </div>
            
            <div style="margin-top: 8mm;">
                <p><span class="checkbox"></span> <strong>Intro to Variables complete</strong></p>
            </div>
            
            <div class="page-number">Page 8</div>
        </div>

        <!-- PAGE 9: DEMO EXERCISE 1 -->
        <div class="page" data-section="var">
            <div class="page-header" style="border-color: #4facfe;">
                <div class="page-title" style="color: #4facfe;">Demonstration Exercises</div>
                <div class="page-subtitle">Watch and Follow Along (Don't Do These Alone Yet)</div>
            </div>
            
            <div class="demo-exercise">
                <h4 style="color: #2196f3; font-size: 18px; margin-bottom: 3mm;">👨‍🏫 Demo 1: Create a Variable</h4>
                
                <p><strong>Watch me do this first:</strong></p>
                
                <div class="code-block">let color = "blue";<br>console.log(color);<br><br>// Output: blue</div>
                
                <p style="margin-top: 5mm;"><strong>What happened here:</strong></p>
                <ol>
                    <li>We created a box (variable) called <code>color</code></li>
                    <li>We put the word "blue" inside it</li>
                    <li>We asked the program to show us what's in the box</li>
                    <li>The program printed: <code>blue</code></li>
                </ol>
                
                <div class="visual-placeholder" style="height: 40mm; margin: 5mm 0;">
                    [DIAGRAM: Box labeled "color" with arrow pointing to it labeled "create"<br>
                    Box contains "blue"<br>
                    Arrow pointing out labeled "read"]
                </div>
                
                <div class="box" style="background: #e8f5e9;">
                    <p><strong>Key Points:</strong></p>
                    <ul>
                        <li><code>let</code> means "create a new variable"</li>
                        <li><code>color</code> is the name (label) we chose</li>
                        <li><code>= "blue"</code> means "put this value in the box"</li>
                        <li>Words (strings) must have quotes around them</li>
                    </ul>
                </div>
            </div>
            
            <div class="demo-exercise" style="margin-top: 8mm;">
                <h4 style="color: #2196f3; font-size: 18px; margin-bottom: 3mm;">👨‍🏫 Demo 2: Change the Value</h4>
                
                <p><strong>Now watch what happens when we change it:</strong></p>
                
                <div class="code-block">let color = "blue";<br>console.log(color);  // shows: blue<br><br>color = "red";<br>console.log(color);  // shows: red</div>
                
                <p style="margin-top: 5mm;"><strong>What happened:</strong></p>
                <ol>
                    <li>First we created <code>color</code> with "blue"</li>
                    <li>We checked what's inside — it showed "blue"</li>
                    <li>Then we <strong>changed</strong> it to "red" (notice: no <code>let</code> this time!)</li>
                    <li>We checked again — now it shows "red"</li>
                </ol>
                
                <div class="box" style="background: #fff3e0; margin-top: 5mm;">
                    <p><strong>Important:</strong> You only use <code>let</code> when <em>creating</em> a variable for the first time. After that, just use the variable name to change it.</p>
                </div>
            </div>
            
            <div class="page-number">Page 9</div>
        </div>

        <!-- PAGE 10: DEMO EXERCISES 3-4 -->
        <div class="page" data-section="var">
            <div class="page-header" style="border-color: #4facfe;">
                <div class="page-title" style="color: #4facfe;">Demonstration Exercises (continued)</div>
            </div>
            
            <div class="demo-exercise">
                <h4 style="color: #2196f3; font-size: 18px; margin-bottom: 3mm;">👨‍🏫 Demo 3: Working with Numbers</h4>
                
                <p><strong>Variables can store numbers too:</strong></p>
                
                <div class="code-block">let score = 0;<br>console.log(score);  // shows: 0<br><br>score = 10;<br>console.log(score);  // shows: 10</div>
                
                <p style="margin-top: 5mm;"><strong>Key Difference:</strong></p>
                <div class="two-column" style="gap: 5mm;">
                    <div class="box" style="background: #e3f2fd;">
                        <p style="margin: 0;"><strong>Text (strings):</strong><br>Need quotes<br><code>"blue"</code> <code>"hello"</code></p>
                    </div>
                    <div class="box" style="background: #fce4ec;">
                        <p style="margin: 0;"><strong>Numbers:</strong><br>No quotes<br><code>0</code> <code>10</code> <code>-5</code></p>
                    </div>
                </div>
            </div>
            
            <div class="demo-exercise" style="margin-top: 8mm;">
                <h4 style="color: #2196f3; font-size: 18px; margin-bottom: 3mm;">👨‍🏫 Demo 4: Math with Variables</h4>
                
                <p><strong>We can do math with number variables:</strong></p>
                
                <div class="code-block">let score = 0;<br>console.log(score);  // 0<br><br>score = score + 5;<br>console.log(score);  // 5<br><br>score = score + 3;<br>console.log(score);  // 8</div>
                
                <p style="margin-top: 5mm;"><strong>What <code>score = score + 5</code> means:</strong></p>
                <ol>
                    <li>Look at what's currently in <code>score</code> (it's 0)</li>
                    <li>Add 5 to it (0 + 5 = 5)</li>
                    <li>Put the result back into <code>score</code></li>
                </ol>
                
                <div class="visual-placeholder" style="height: 35mm; margin-top: 5mm;">
                    [DIAGRAM: Three boxes showing transformation<br>
                    Box 1: score = 0<br>
                    Arrow with "+5"<br>
                    Box 2: score = 5<br>
                    Arrow with "+3"<br>
                    Box 3: score = 8]
                </div>
            </div>
            
            <div class="page-number">Page 10</div>
        </div>

        <!-- PAGE 11: DEMO EXERCISE 5 -->
        <div class="page" data-section="var">
            <div class="page-header" style="border-color: #4facfe;">
                <div class="page-title" style=" ...... program stopped here ? 