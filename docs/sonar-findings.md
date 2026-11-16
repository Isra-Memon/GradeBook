
# Lab 10 – SonarCloud Static Code Analysis Findings

## Project Information
- Project: GradeBook
- GitHub Repository: Isra-Memon/GradeBook
- Branch: main
- Analysis Tool: SonarQube Cloud
- Analysis Date: 16 November 2026

## Objective
To perform static code analysis on the GradeBook project using SonarCloud, identify potential code quality issues, and evaluate the project's Quality Gate status.

## SonarCloud Configuration
The sonar-project.properties file was added to the repository to configure source code analysis, test directories, and the Python version.

## Analysis Results

| Metric | Result |
|---|---|
| Lines of Code | 238 |
| Quality Gate | Passed |
| Reported Issues | 0 |
| Code Duplication | 0.0% |
| Coverage | No data available |
| Analysis Warnings | 2 |

## Issue Triage
The Issues page was reviewed with all filters cleared.

No issues were reported in the current analysis. Therefore, no issue-specific rule IDs, file locations, severities, or risks could be listed.

## Analysis Warnings
1. Python version: SonarCloud initially used a default Python version range instead of an explicitly configured version.
2. Test configuration: SonarCloud initially detected test files without an explicit sonar.tests setting.

The configuration file was added to address these settings. The latest dashboard still displays two warnings, so their resolution remains unverified.

## Bug and Vulnerability Fixes
No bugs or vulnerabilities were reported by the current SonarCloud analysis. No issue-specific fixes were performed.

## Code Smells and Duplication
No code smells were listed on the unfiltered Issues page. The dashboard reported 0.0% duplication.

No refactoring fixes have been performed as part of this lab yet.

## Quality Gate Verification
After the configuration file was committed, SonarCloud performed a new analysis.

The Quality Gate status changed from "Not computed" to "Passed".

## Pending Verification
- Resolve or document remaining analysis warnings.
- Run the full pytest suite.
- Complete any additional issue-fixing exercises required by the instructor.
- Prepare before-and-after evidence.

## Conclusion
SonarCloud was successfully connected to the GradeBook repository. The latest analysis reported zero issues and zero duplication, and the Quality Gate passed. Test coverage and remaining verification activities will be addressed separately.
