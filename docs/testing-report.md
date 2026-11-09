
# UGM Calculator — Manual Testing Report

## 1. Test Overview

**Project:** UGM Calculator  
**GitHub Issue:** #14 — Test the Application and Improve Documentation  
**Test Date:** 6 November 2026  
**Test Type:** Manual Functional and User Interface Testing  
**Overall Result:** PASS

### Objective

To verify that the UGM Calculator launches successfully, performs mathematical operations correctly, handles invalid calculations, maintains calculation history and provides a usable interface.

## 2. Test Results

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC-01 | Application Launch | Application opens with display, buttons and history visible | Application launched successfully | PASS |
| TC-02 | Basic Arithmetic | Addition, subtraction, multiplication and division return correct results | All four operations returned expected results | PASS |
| TC-03 | Clear Button | Current calculation is cleared and display resets to 0 | Display reset to 0 | PASS |
| TC-04 | Backspace Button | Last digit is removed | 12345 changed to 1234 | PASS |
| TC-05 | Decimal Calculations | Decimal calculations return correct results | All three calculations passed | PASS |
| TC-06 | Negative Numbers | Negative number calculations return correct results | All three calculations passed | PASS |
| TC-07 | Division by Zero | Error message is displayed without crashing | Displayed "Cannot divide by zero" | PASS |
| TC-08 | Calculation History | Completed calculations appear in history | Both test calculations appeared correctly | PASS |
| TC-09 | Clear History | History is cleared and calculator remains functional | History cleared; calculator continued working | PASS |
| TC-10 | Window Resizing | Layout remains usable at supported window sizes | All components remained visible and aligned | PASS |

## 3. Test Data

### Basic Arithmetic
- 8 + 4 = 12
- 9 − 5 = 4
- 6 × 3 = 18
- 8 ÷ 2 = 4

### Decimal Calculations
- 2.5 + 1.3 = 3.8
- 5.5 − 2.2 = 3.3
- 2.5 × 2 = 5

### Negative Number Calculations
- 5 − 10 = -5
- 5 − (-3) = 8
- (-4) × 3 = -12

### Calculation History
- 8 + 2 = 10
- 6 × 3 = 18

## 4. Bugs and Issues

No bugs were identified during the manual testing activities documented in this report.

## 5. Test Summary

- Total test cases: 10
- Passed: 10
- Failed: 0
- Blocked: 0

All planned manual test cases passed successfully.

## 6. Conclusion

The UGM Calculator successfully passed the documented manual functional and interface tests.

The application demonstrated correct arithmetic calculations, input controls, error handling, calculation history management and layout usability.

These results support preparation for the final project demonstration.
