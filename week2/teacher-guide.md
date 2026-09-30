# Class 2 teacher guide

**Topic:** motion in one dimension.  
**Audience:** second-week students who have completed units and conversions and have just started programming. Assume algebra, not calculus.  
**Total:** 180 minutes: a 90-minute lecture and a 90-minute workshop, each including a five-minute break.

## Open these files

- Teach from [lecture.md](lecture.md).
- Give students [workshop.md](workshop.md) and the images it references.
- Keep [solutions.md](solutions.md) for feedback and marking after attempts.
- Use the [course index](../README.md) to locate the original PDFs and teacher archive.

All teaching documents are Markdown. They use ordinary headings, tables, Unicode mathematical symbols, and local PNGs; no slide framework, equation plugin, internet access, or special Markdown extension is required. Open them in a Markdown preview. If printing, check the preview first and have students write full solutions on separate paper.

For a student distribution, copy lecture.md, workshop.md, and the assets folder together. The assets folder also contains answer visuals: omit **workshop-graph-solution.png/.svg** and **python-comparison.png/.svg** until after students have attempted the corresponding work. Do not distribute this guide, solutions.md, or the course teacher ZIP in advance.

## Before students arrive

1. Open both student documents in Markdown preview and check that their images load.
2. Have paper, pens, a board or document camera, and practice calculators available. Today's use of aids does not establish exam permissions.
3. Open the Q7 code in the same Python environment already used in programming class. Run the original example once, then restore it to acceleration = 1.0 and time = 4.0. No packages are required.
4. If students lack a working environment, plan to run Q7 yourself with students predicting every output on paper. Do not spend lesson time installing software.
5. On the board write: **Choose direction → convert units → choose equation → show working → check.**
6. Keep the original Week 3 label on Exercise 3. Explain that selected 1D questions are being used in our second class.

The source course information dates from 2024 and describes an optional-exam grade-improvement arrangement. The current brief is preparation for an end-of-course written exam. Do not repeat the historical grading arrangement as current policy. Calculator and formula-sheet permissions are still unconfirmed.

## Learning evidence to collect

| Outcome | Evidence during the lesson | Evidence in the workshop |
|---|---|---|
| Distinguish position, distance, and displacement | Return-trip prediction and robot example | Q2 and Q4 |
| Distinguish speed and signed velocity | Explain a negative velocity | Q2, Q7, exit ticket |
| Read graph slopes and signed areas | Interpret Figures 2–3 | Q3, Q4, Q8 |
| Choose constant-acceleration equations | Explain why a formula fits the cart model | Q5, Q6, Q8 |
| Present a written physics solution | Givens, direction, equation, units, check | Collect Q8 |
| Interpret a simple calculation in Python | Predict before running | Q7 written explanation |

Do not grade coding fluency here. Use Python to compare the same physical equations with students' paper calculations.

## Lecture delivery: minutes 0–90

| Time | What to do | Checkpoint or prompt |
|---|---|---|
| 0–10 | Give three retrieval questions, then model unit cancellation and the written method. | 72 km/h = 20 m/s; 250 ms = 0.250 s. |
| 10–25 | Use the motion path. Let students trace the outbound and return segments before introducing the two averages. Spend the last few minutes on unequal-time averaging. | “Which part of the journey adds to distance but subtracts from displacement?” |
| 25–35 | Read axes on the position graph; construct the slope triangle. Have students compare graph height with slope. | “What are the units of the vertical axis? What are the units of rise divided by run?” |
| 35–45 | Move to velocity–time slope and area. Ask for the rectangle and triangle separately. | Acceleration +1 m/s²; displacement 16 m. |
| 45–50 | Break. | Leave the two graph rules on the board. |
| 50–58 | Connect the three motion graphs and build the equations from velocity change and area. | Ask why the acceleration contribution contains t². |
| 58–70 | Work the stopping-cart example one line at a time. Use a graph as an independent check. Briefly show the no-time equation. | a = −2 m/s²; Δx = +9 m. |
| 70–75 | Use the sign chart; ask for a case where negative acceleration increases speed. | v < 0 and a < 0. |
| 75–81 | Set the robot example: three minutes alone, one minute in pairs, then reveal the calculation. | v = 4 m/s; Δx = 12 m; x = 13 m. |
| 81–85 | Introduce free fall through coordinates and signs, using the one-second example. | Height can remain positive while velocity is negative. |
| 85–90 | Run the five short checks and introduce the workshop. | Correct misconceptions before asking for independent calculations. |

**Useful language:** “A sign tells us a direction relative to our chosen axis.” “Tell me what the axes mean before interpreting the line.” “Which quantity did you calculate: position, displacement, or distance?”

The lecture contains answers after prompts. Reveal a section at a time or cover the answer while students work. Use the student workshop for assessment attempts without visible worked solutions.

## Workshop delivery: minutes 90–180

The student worksheet uses its own 0–90 minute clock.

| Workshop clock | Whole-class clock | Facilitation |
|---|---|---|
| 0–10 | 90–100 | Q1–Q2. Begin independently; use a brief pair comparison before a quick answer check. |
| 10–30 | 100–120 | Q3 for about 12 minutes, Q4 for about 8. Ask students to write slope and area units. |
| 30–50 | 120–140 | Q5 for about 8 minutes, Q6 for about 12. Insist on converting aircraft speed first and retaining digits. |
| 50–55 | 140–145 | Break. |
| 55–70 | 145–160 | Q7: four minutes prediction, four minutes first run, seven minutes changes and explanation. Swap pair roles. |
| 70–80 | 160–170 | Q8 alone, without Python. Use today's learning formula card. Collect or inspect each person's solution. |
| 80–87 | 170–177 | Reveal Q8; students correct in another colour and explain one correction. |
| 87–90 | 177–180 | Exit ticket. Collect it for planning class 3. |

### Facilitation when students are stuck

Ask for one next step rather than giving the answer:

- Q2: “Mark the starting position and finish on the number line.”
- Q3: “Is this asking for a slope, a height, or an area?”
- Q4: “Choose two points. What changes between them?”
- Q5: “Which values are known? Which equation contains your unknown?”
- Q6: “What does reaching rest tell you about the final velocity?”
- Q7: “Read the first four lines aloud with units. Which one did you change?”
- Q8: “Show a valid equation even if you cannot finish the arithmetic.”

### Beginner Python boundaries

Students copy a complete block, change numeric values, and rerun the whole block. Explain only assignment, multiplication, powers, comments, and printing as needed. They do not need to write functions, loops, lists, or plot commands.

If typing or environment trouble lasts more than two minutes, switch to the teacher demonstration. Each student still predicts and explains the three cases. Use the prepared [comparison graph](assets/python-comparison.png) after predictions. The old kinematics workshop is an optional later resource; it assumes substantially more programming knowledge.

## Misconceptions and responses

| Student claim | Quick response |
|---|---|
| “Final position equals distance travelled.” | Use a nonzero starting position and a return segment. Ask for all three quantities separately. |
| “A horizontal graph means the object stopped.” | Ask which quantity is on the vertical axis. Horizontal position means rest; horizontal velocity means constant velocity. |
| “The graph slopes down, so the object moves left.” | On a velocity graph, check whether velocity is below zero. A downward slope alone indicates negative acceleration. |
| “Zero average acceleration means velocity never changed.” | Revisit Q3, where start and finish velocities match. |
| “Negative acceleration always slows the object.” | Compare v = −2 m/s with a = −1 m/s²: speed increases. |
| “At the turn, both velocity and acceleration are zero.” | In Q7 at 2 s, v = 0 but a = −1 m/s². |
| “Average velocity is always the mean of the endpoint velocities.” | State the constant-acceleration condition. Q3 is a counterexample. |
| “A program running successfully proves the physics.” | Ask for a unit check and a paper checkpoint. |
| “The braking equation predicts the object remains parked.” | Explain that constant negative acceleration beyond stopping predicts reversal. End the model at rest. |

## Pacing, support, and extension

The timings include transitions, short comparisons, and checks. Free fall is introductory in the lecture; extended fall calculations, reversal areas, and the no-time problem are optional follow-up.

If students need longer, defer the lecture's unequal-time cyclist example and the alternative no-time calculation. In the workshop, prioritise Q2, Q3(a–e), Q5(a–c), Q6(a–c), the teacher-led Q7 comparison, and the individual Q8. Move remaining subparts to follow-up rather than rushing the independent written evidence.

If students finish early, use the Q3 average-velocity question, then E2, E1, and E3. Keep the next class's vector and projectile topics out of this core lesson.

## After class

Use Q8 and the exit ticket to group next steps: unit conversions, graph meaning, sign conventions, equation choice, or written presentation. A student who computes correctly but confuses position and displacement still needs conceptual practice.

Release the solutions after attempts. Suggested follow-up is to correct one missed core question and complete E1 or E3 with full written working. E2 is especially useful for students who confuse signed area and distance. Use the review sheet later as transfer practice; it also contains topics not yet taught.

## Source alignment

- [Full lecture notes](../course/reference/Physics%20Period1%20Lect%20%282%29.pdf): pages 2–8 cover straight-line motion, slope, area, acceleration, braking, and gravity. Pages 9 onward introduce later vector and projectile material.
- [Formula sheet](../course/reference/PhysicsOrientationFormulas.pdf): use sections 0.1–0.3. The source sometimes writes x where the starting position is zero; this lesson uses Δx explicitly.
- [Exercise 3](../course/exercises/Physics%20Period1%20Exer3.pdf): Q5 supplies the aircraft scenario; Q3 supplies the optional well problem.
- [Review exercises](../course/exercises/Physics%20Period1%20ReviewExer.pdf): Q2 motivates graph interpretation; Q3 provides the lecture's unequal-duration cyclist example.
- [Physics motivation](../course/reference/Why%20study%20Physics.pdf): informs the robot and software connections.

This pack uses g = 9.81 m/s² consistently. Original sources sometimes use 9.8; accept a consistently stated value when comparing old solutions. All new visuals are purpose-made; the original PDFs and archive have been preserved unchanged.
