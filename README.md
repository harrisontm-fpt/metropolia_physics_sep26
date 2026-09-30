# Physics course materials

## Start here

For the second class, open the [teacher guide](week2/teacher-guide.md), then teach from the [visual lecture](week2/lecture.md). Give students the [workshop](week2/workshop.md); use the separate [worked solutions](week2/solutions.md) after their attempts.

Class 2 lasts three hours, split equally between lecture and workshop, including two five-minute breaks. It builds on units and conversions, assumes algebra without calculus, and supports the end-of-course written exam. Its short Python activity is suitable for programming beginners.

## Folder guide

| Folder | Contents |
|---|---|
| [week1](week1/) | First-class units/conversions guide, Exercise 1, conversion Python starter, and conversion images |
| [week2](week2/) | New Markdown lecture, workshop, teacher guide, solutions, and visual assets |
| [course/reference](course/reference/) | Original course-wide lecture notes, formula sheet, historical course information, and motivation |
| [course/exercises](course/exercises/) | Original later-week exercise sheets and course review |
| [course/optional-python](course/optional-python/) | Original kinematics starter for later use once students know functions, lists, and loops |
| [course/teacher](course/teacher/) | Original ZIP containing teacher notes, completed code, and reference plots |

The empty original real_world_cases.txt remains in week1 to avoid deleting a source file. The course-wide PDFs describe the supplied Period 1 material; this organisation does not assume that they cover every later period.

## Class 1 resources

- [Week 1 teacher guide](week1/Physics_Period_1_Week_1_Teacher_Guide.docx)
- [Exercise 1: measurements and conversions](week1/Physics%20Period1%20Exer1.pdf)
- [Conversion workshop starter](week1/conversion_workshop.py)

The conversion images remain alongside the starter, preserving its local output convention. Original DOCX, PDF, Python, PNG, and ZIP contents were not rewritten.

## Relocated resources

All files below previously lived directly inside week1. Their original filenames and exercise identifiers are preserved.

| Original filename | Current location |
|---|---|
| Physics Period1 Lect (2).pdf | [Course lecture notes](course/reference/Physics%20Period1%20Lect%20%282%29.pdf) |
| PhysicsOrientationFormulas.pdf | [Formula sheet](course/reference/PhysicsOrientationFormulas.pdf) |
| Software1 Physics 2024ABC Info.pdf | [Historical course information](course/reference/Software1%20Physics%202024ABC%20Info.pdf) |
| Why study Physics.pdf | [Physics motivation](course/reference/Why%20study%20Physics.pdf) |
| Physics Period1 Exer3.pdf | [Exercise 3](course/exercises/Physics%20Period1%20Exer3.pdf) |
| Physics Period1 Exer4.pdf | [Exercise 4](course/exercises/Physics%20Period1%20Exer4.pdf) |
| Physics Period1 Exer5.pdf | [Exercise 5](course/exercises/Physics%20Period1%20Exer5.pdf) |
| Physics Period1 ReviewExer.pdf | [Review exercises](course/exercises/Physics%20Period1%20ReviewExer.pdf) |
| kinematics_1d_workshop.py | [Optional kinematics starter](course/optional-python/kinematics_1d_workshop.py) |
| physics_workshops_teacher_pack.zip | [Teacher archive](course/teacher/physics_workshops_teacher_pack.zip) |

Original documents and archive notes may mention resources by their old names or locations; use this table to find them. The intact teacher archive includes solutions for both original Python workshops and is not a student handout.

Exercise 3 is labelled Week 3 in the source. The new second-class workshop deliberately selects its appropriate 1D questions. There was no Exercise 2 file among the supplied materials; no replacement source sheet or changed numbering is implied.

The 2024 course information includes an older optional-exam grading arrangement. It is retained as source material, not asserted as current policy. The new pack follows the current written-exam preparation brief; calculator and formula-sheet permissions remain unconfirmed.

## Viewing, sharing, and editing the new materials

Open Markdown files in a preview that supports standard tables and local images. Mathematical expressions use readable text and Unicode symbols rather than requiring a LaTeX extension. Work can be completed on separate paper; the student worksheet does not include worked answers.

Keep relative folders intact when sharing. Distribute lecture.md and workshop.md with their referenced images. Hold back solutions.md, teacher-guide.md, workshop-graph-solution images, python-comparison images, and course/teacher until appropriate.

The visuals in week2/assets include PNGs for broad Markdown compatibility and editable SVG equivalents. The optional [visual builder](week2/tools/build_visuals.mjs) reproduces them with Node.js and the sharp package available to the builder. It is an authoring utility, not a student prerequisite. When sharp is available through normal Node resolution, run `node week2/tools/build_visuals.mjs`; alternatively pass the file URL of an installed sharp module as the first argument.

The lecture and student workshop are usable offline. Original source links remain local.
