
# UGM Calculator — User Guide

## 1. Introduction

UGM Calculator is a desktop application developed using Python and CustomTkinter.

This guide explains how to use the calculator's main features.

## 2. Launching the Application

After completing the installation steps in the README.md file, activate the virtual environment and run:

```bash
python main.py
```

The calculator window will open.

## 3. Basic Calculations

The calculator supports four arithmetic operations:

| Operation | Symbol | Example |
|---|---|---|
| Addition | + | 8 + 4 = 12 |
| Subtraction | − | 9 − 5 = 4 |
| Multiplication | × | 6 × 3 = 18 |
| Division | ÷ | 8 ÷ 2 = 4 |

Enter the numbers and select the required operation. Press `=` to display the result.

## 4. Decimal and Negative Numbers

The calculator supports decimal values and negative numbers.

Examples:

- 2.5 + 1.3 = 3.8
- 5 − 10 = -5
- (-4) × 3 = -12

## 5. Parentheses

Parentheses can be used to group mathematical expressions.

Example:

(5 + 3) × 2 = 16

The expression inside the parentheses is evaluated first.

## 6. Clear and Backspace

### Clear (C)

Press `C` to clear the current calculation and reset the display to 0.

### Backspace (⌫)

Press `⌫` to remove the last character entered.

For example, entering 12345 and pressing Backspace changes the input to 1234.

## 7. Calculation History

Completed calculations are displayed in the history section.

This allows users to review previous calculations and their results.

### Clear History

Press the Clear History button to remove previous calculation entries.

Clearing the history does not prevent further calculations.

## 8. Result Formatting

Results are displayed with up to one decimal place.

Examples:

- 10 ÷ 2 = 5
- 7 ÷ 3 = 2.3

Unnecessary trailing zeros are removed.

## 9. Error Handling

The calculator handles invalid operations without closing unexpectedly.

For example, dividing by zero displays:

`Cannot divide by zero`

## 10. Troubleshooting

If the application does not launch:

1. Confirm that Python is installed.
2. Ensure the virtual environment is activated.
3. Install the dependencies using `python -m pip install -r requirements.txt`.
4. Run the application using `python main.py`.

## 11. Testing

The application has passed 10 manual test cases covering its main functionality.

For detailed results, see the [Manual Testing Report](testing-report.md).
