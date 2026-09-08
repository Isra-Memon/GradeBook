
# Equivalence Partitioning Analysis — GradeBook

## 1. letter_grade(score) — Worked Example

| Class | Range | Valid/Invalid | Representative |
|---|---|---|---|
| Invalid-low | score < 0 | Invalid | -10 |
| F | 0-59 | Valid | 45 |
| D | 60-69 | Valid | 65 |
| C | 70-79 | Valid | 75 |
| B | 80-89 | Valid | 85 |
| A | 90-100 | Valid | 95 |
| Invalid-high | score > 100 | Invalid | 150 |

## 2. Scores Count per Student

Rule: a student must have between 1 and 6 scores.

| Class | Range | Valid/Invalid | Representative |
|---|---|---|---|
| Too few | 0 scores | Invalid | 0 |
| Valid range | 1-6 scores | Valid | 3 |
| Too many | 7+ scores | Invalid | 8 |

## 3. Student Name Field

Rule: non-empty string, max 50 characters, letters/spaces/hyphens only.

| Class | Description | Valid/Invalid | Representative |
|---|---|---|---|
| Valid typical name | Normal name within length limit | Valid | "Ali Khan" |
| Empty string | No characters | Invalid | "" |
| Over-length string | More than 50 characters | Invalid | "A" * 51 |
| Contains digits/symbols | Non-letter characters present | Invalid | "Ali123!" |

## EP Limitation Note

Equivalence Partitioning only tests one representative value per class, so it can miss off-by-one (boundary) errors — e.g. exactly 0, 1, 6, or 7 scores, or a name of exactly 50 or 51 characters. This gap is addressed in Lab 6 using Boundary Value Analysis.

## Pytest Run Summary (Full Suite)

```
collected 14 items

tests/test_letter_grade.py::test_letter_grade_valid_classes[45-F] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[65-D] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[75-C] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[85-B] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[95-A] PASSED
tests/test_letter_grade.py::test_letter_grade_invalid_classes[-10] PASSED
tests/test_letter_grade.py::test_letter_grade_invalid_classes[150] PASSED
tests/test_roster.py::test_roster_add_student_score_count[0] PASSED
tests/test_roster.py::test_roster_add_student_score_count[3] PASSED
tests/test_roster.py::test_roster_add_student_score_count[8] PASSED
tests/test_validate_name.py::test_validate_name_valid_typical PASSED
tests/test_validate_n
