# Requirements Traceability Matrix — GradeBook

| Requirement ID | Description | Linked Test Case(s) |
|-----------------|--------------|----------------------|
| REQ-1 | Reject negative scores | TC-002, TC-003, TC-007 |
| REQ-2 | Return 0.0 average for empty scores | TC-005 |
| REQ-3 | Reject duplicate roll numbers | TC-013 |
| REQ-4 | Case-insensitive student search | TC-008 |
| REQ-5 | Correctly compute individual average | TC-001, TC-004, TC-006 |
| REQ-6 | Correctly compute class average | TC-014 |
| REQ-7 | Accept only scores between 0-100 | TC-009, TC-010 |
| REQ-8 | Assign letter grade based on average | TC-011, TC-012 |

## Coverage Gaps Identified
- **REQ-3** had zero linked test cases initially. Added **TC-013** to close this gap.
- **REQ-6** had zero linked test cases initially. Added **TC-014** to close this gap.
