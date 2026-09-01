# Test Cases — GradeBook

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type |
|----|-------|-------------|----------------|-------|----------|----------|------|
| TC-001 | Add valid score | REQ-5 | Student object exists with empty scores | 1. Call student.add_score(85) | Score 85 is added to scores list | High | Functional |
| TC-002 | Reject negative score | REQ-1 | Student object exists with empty scores | 1. Call student.add_score(-5) | A ValueError is raised and scores remains empty | High | Negative |
| TC-003 | Reject non-numeric score | REQ-1 | Student object exists with empty scores | 1. Call student.add_score("abc") | A TypeError or ValueError is raised | Medium | Negative |
| TC-004 | Average with multiple scores | REQ-5 | Student has scores [80, 90] | 1. Call student.average() | Returns 85.0 | High | Functional |
| TC-005 | Average with empty scores list | REQ-2 | Student object exists with no scores added | 1. Call student.average() | Returns 0.0, no error raised | High | Boundary |
| TC-006 | Average with a single score | REQ-5 | Student has one score [75] | 1. Call student.average() | Returns 75.0 | Medium | Functional |
| TC-007 | Reject negative score on add_score() | REQ-1 | A Student object exists with an empty scores list | 1. Call student.add_score(-5) | A ValueError is raised and scores remains empty | High | Negative |
| TC-008 | Name search case-insensitivity | REQ-4 | GradeBook has a student named "Isra" | 1. Call gb.find_student("isra") | Returns the Isra student object | Medium | Functional |
| TC-009 | Maximum score boundary (100) | REQ-7 | Student object exists with empty scores | 1. Call student.add_score(100) | Score 100 is accepted and added | Medium | Boundary |
| TC-010 | Minimum score boundary (0) | REQ-7 | Student object exists with empty scores | 1. Call student.add_score(0) | Score 0 is accepted and added | Medium | Boundary |
| TC-011 | Grade-letter conversion, mid-range score | REQ-8 | Student has average of 85 | 1. Call student.grade_letter() | Returns "B" | Medium | Functional |
| TC-012 | Grade-letter conversion at boundary | REQ-8 | Student has average of exactly 90 | 1. Call student.grade_letter() | Returns "A" | Medium | Boundary |
