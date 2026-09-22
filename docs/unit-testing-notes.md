# Unit Testing Notes — pytest Output Comparison

## `pytest -v` (verbose output)

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: GradeBook
configfile: pytest.ini
testpaths: tests
plugins: mock-3.15.1
collected 54 items

tests/test_add_score.py::test_add_score_edge_cases[lowest-valid-score] PASSED [  1%]
tests/test_add_score.py::test_add_score_edge_cases[highest-valid-score] PASSED [  3%]
tests/test_add_score.py::test_add_score_edge_cases[mid-range-score] PASSED [  5%]
tests/test_add_score.py::test_add_score_edge_cases[negative-score-invalid] PASSED [  7%]
tests/test_add_score.py::test_add_score_edge_cases[above-max-invalid] PASSED [  9%]
tests/test_add_score.py::test_add_score_edge_cases[decimal-score-valid] PASSED [ 11%]
tests/test_gradebook_average.py::test_class_average_rounding_boundary PASSED [ 12%]
tests/test_gradebook_average.py::test_class_average_empty_gradebook PASSED [ 14%]
tests/test_gradebook_average.py::test_class_average_single_student PASSED [ 16%]
... (all letter_grade, roster, save_to_file, and validate_name tests) ...
tests/test_validate_name.py::test_validate_name_length_boundaries[51] PASSED [100%]

============================== 54 passed in 0.05s ==============================
```

## `pytest --tb=short` (short output)

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: GradeBook
configfile: pytest.ini
testpaths: tests
plugins: mock-3.15.1
collected 54 items

tests/test_add_score.py ......                                           [ 11%]
tests/test_gradebook_average.py ...                                      [ 16%]
tests/test_letter_grade.py .......                                       [ 29%]
tests/test_letter_grade_bva.py ..................                        [ 62%]
tests/test_roster.py .........                                           [ 79%]
tests/test_save_to_file.py ..                                            [ 83%]
tests/test_validate_name.py .........                                    [100%]

============================== 54 passed in 0.06s ==============================
```

## When to use which

- **`-v` (verbose)**: use while actively writing/debugging tests, or when reviewing a PR — it names every individual test (including each parametrized case via its `id`), so you know exactly which scenario failed.
- **`--tb=short`**: use in CI or when running the full suite quickly — one dot per passing test keeps the output compact, and a shortened traceback (instead of pytest's full multi-line trace) still tells you which line failed without flooding the log.

## Fixture scopes used in this suite

- `empty_roster` (function scope, default): fresh `Roster` for every test — needed because each test mutates it with a different number of scores.
- `rounding_gradebook` (module scope): built once and reused, since its data is fixed and never mutated by the tests that read it.

## Project structure (post-refactor)

Source code was reorganized into a `src/` package with one class per file, and `pytest.ini` sets `pythonpath = src` so tests keep importing via `from gradebook import ...` unchanged.
