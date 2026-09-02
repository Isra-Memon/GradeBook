# Test Cases — GradeBook

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type | Result |
|----|-------|-------------|----------------|-------|----------|----------|------|--------|
| TC-001 | Add valid score | REQ-5 | Student object exists with empty scores | 1. Call student.add_score(85) | Score 85 is added to scores list | High | Functional | Pass |
| TC-002 | Reject negative score | REQ-1 | Student object exists with empty scores | 1. Call student.add_score(-5) | A ValueError is raised and scores remains empty | High | Negative | **Fail — Issue #2** |
| TC-003 | Reject non-numeric score | REQ-1 | Student object exists with empty scores | 1. Call student.add_score("abc") | A TypeError or ValueError is raised | Medium | Negative | **Fail — Issue #10** |
| TC-004 | Average with multiple scores | REQ-5 | Student has scores [80, 90] | 1. Call student.average() | Returns 85.0 | High | Functional | Pass |
| TC-005 | Average with empty scores list | REQ-2 | Student object exists with no scores added | 1. Call student.average() | Returns 0.0, no error raised | High | Boundary | Pass |
| TC-006 | Average with a single score | REQ-5 | Student has one score [75] | 1. Call student.average() | Returns 75.0 | Medium | Functional | Pass |
| TC-007 | Reject negative score on add_score() | REQ-1 | A Student object exists with an empty scores list | 1. Call student.add_score(-5) | A ValueError is raised and scores remains empty | High | Negative | **Fail — Issue #2** |
| TC-008 | Name search case-insensitivity | REQ-4 | GradeBook has a student named "Isra" | 1. Call gb.find_student("isra") | Returns the Isra student object | Medium | Functional | Pass |
| TC-009 | Maximum score boundary (100) | REQ-7 | Student object exists with empty scores | 1. Call student.add_score(100) | Score 100 is accepted and added | Medium | Boundary | Pass |
| TC-010 | Minimum score boundary (0) | REQ-7 | Student object exists with empty scores | 1. Call student.add_score(0) | Score 0 is accepted and added | Medium | Boundary | Pass |
| TC-011 | Grade-letter conversion, mid-range score | REQ-8 | Student has average of 85 | 1. Call student.grade_letter() | Returns "B" | Medium | Functional | Pass |
| TC-012 | Grade-letter conversion at boundary | REQ-8 | Student has average of exactly 90 | 1. Call student.grade_letter() | Returns "A" | Medium | Boundary | Pass |
| TC-013 | Reject duplicate roll number | REQ-3 | GradeBook has a student with roll_no 101 | 1. Call gb.add_student(Student("Ahmed", 101)) | A ValueError is raised, second student not added | High | Negative | Pass |
| TC-014 | Class average with multiple students | REQ-6 | GradeBook has 2 students each with scores | 1. Call gb.class_average() | Returns the correct mean of all students' averages | Medium | Functional | Pass |

## Summary
- **Total:** 14 test cases
- **Pass:** 11
- **Fail:** 3 (TC-002, TC-003, TC-007) — all linked to open GitHub Issues (#2, #10)
