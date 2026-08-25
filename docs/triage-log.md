# Triage Log — GradeBook v0.2

## Fix Order (Priority Order)

1. **Bug #1 — Crash on empty score list** (severity:high, priority:P1)
   App completely crashes, must fix first — blocks basic usage.

2. **Bug #3 — Duplicate roll numbers allowed** (severity:high, priority:P1)
   Corrupts data integrity, same priority as Bug #1 but doesn't crash — fixed second.

3. **Bug #5 — Case-sensitive student search** (severity:medium, priority:P2)
   Affects usability but has a workaround (exact case typing).

4. **Bug #2 — Negative scores accepted** (severity:medium, priority:P2)
   Data quality issue, not urgent for this sprint's demo.

5. **Bug #4 — Incorrect rounding of class average** (severity:low, priority:P3)
   Cosmetic accuracy issue, lowest impact.

## Severity vs Priority Trade-off Notes

- **Bug #1 vs Bug #3:** Both are severity:high and priority:P1, but Bug #1 is fixed
  first because a crash blocks ALL functionality, while Bug #3 only corrupts
  specific records — the app still runs.

- **Bug #5 vs Bug #2:** Bug #5 is fixed before Bug #2 despite both being
  priority:P2, because search failing affects every user interaction, while
  negative scores only affect data entered incorrectly (edge case).

## Not Fixing This Sprint

- **Bug #4** (status:wontfix) — Low severity, cosmetic rounding issue only.
  Deferred to next sprint since it doesn't affect core functionality or grades.
- **Bug #2** (status:wontfix) — Medium severity but low frequency in real usage;
  can be addressed in a later data-validation sprint alongside other input checks.
