# Boundary Value Analysis — GradeBook

## 1. letter_grade(score) — Boundary Table

| Boundary | value-1 | value | value+1 | Expected at each |
|---|---|---|---|---|
| Domain low (0) | -1 | 0 | 1 | -1 → Invalid (raises ValueError); 0 → 'F'; 1 → 'F' |
| F/D cut-off (60) | 59 | 60 | 61 | 59 → 'F'; 60 → 'D'; 61 → 'D' |
| D/C cut-off (70) | 69 | 70 | 71 | 69 → 'D'; 70 → 'C'; 71 → 'C' |
| C/B cut-off (80) | 79 | 80 | 81 | 79 → 'C'; 80 → 'B'; 81 → 'B' |
| B/A cut-off (90) | 89 | 90 | 91 | 89 → 'B'; 90 → 'A'; 91 → 'A' |
| Domain high (100) | 99 | 100 | 101 | 99 → 'A'; 100 → 'A'; 101 → Invalid (raises ValueError) |

## 2. Roster.add_student() — Score Count Boundary Table

| Boundary | value-1 | value | value+1 | Expected at each |
|---|---|---|---|---|
| Domain low (1) | 0 | 1 | 2 | 0 → Invalid (raises ValueError); 1 → Valid; 2 → Valid |
| Domain high (6) | 5 | 6 | 7 | 5 → Valid; 6 → Valid; 7 → Invalid (raises ValueError) |


## 3. validate_name(name) — Name Length Boundary Table

| Boundary | value-1 | value | value+1 | Expected at each |
|---|---|---|---|---|
| Domain low (empty) | — | 0 chars | 1 char | 0 → Invalid (raises ValueError, "Name cannot be empty"); 1 → Valid |
| Domain high (50) | 49 chars | 50 chars | 51 chars | 49 → Valid; 50 → Valid; 51 → Invalid (raises ValueError, "too long") |
