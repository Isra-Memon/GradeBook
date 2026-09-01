# Test Plan — GradeBook

## 1. Introduction
This document defines the test plan for the GradeBook module, a small Python library that manages student records, scores, averages, and letter grades. The purpose of testing is to verify that GradeBook meets its functional requirements before further features are added.

## 2. Test Items
- `Student` class (add_score, average, grade_letter)
- `GradeBook` class (add_student, find_student, class_average)

## 3. Features to be Tested
- Adding and validating scores
- Computing individual and class averages
- Duplicate roll number rejection
- Case-insensitive student search
- Letter grade assignment

## 4. Features Not to be Tested
- User interface — GradeBook is a backend library with no UI; there is nothing to test at that layer.
- Persistence/database storage — the current version keeps data in memory only, so no storage layer exists to test.

## 5. Approach
Testing will be manual and black-box, executed directly against the public methods of `Student` and `GradeBook` using a Python shell. Each test case will be traced to a specific requirement (see rtm.md). Both positive (valid input) and negative (invalid/edge-case input) tests will be included.

## 6. Pass/Fail Criteria
A test case passes if the actual result matches the expected result exactly. The release is considered test-ready when at least 95% of planned test cases pass and zero Critical-severity defects remain open.

## 7. Test Deliverables
- test-plan.md (this document)
- test-cases.md (12 test cases)
- rtm.md (requirements traceability matrix)
- GitHub Issues for any failed test cases

## 8. Environmental Needs
Python 3.x installed locally; no external dependencies or database required. Tests can be run using the Python interactive shell or a simple script.

## 9. Schedule
All testing tasks (test case writing, traceability, and execution) are completed within this single lab session (3.0 hours).

## 10. Risks
- Some requirements (REQ-1, REQ-7) may not be fully implemented in the current code, which could cause otherwise-valid test cases to fail.
- Manual execution is prone to human error compared to automated testing.
