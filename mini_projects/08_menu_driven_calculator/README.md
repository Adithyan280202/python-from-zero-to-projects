# Mini Project 08A: Menu-Driven Calculator

## 1. Project Overview

The Menu-Driven Calculator is a beginner-friendly Python project that performs four basic arithmetic operations based on the user's selection.

The program accepts two numbers, displays an operation menu, and uses conditional statements to perform the selected calculation.

This project provides practical experience with decision-making in Python.

## 2. Learning Objectives

By completing this project, you will learn:

- How to use `if`, `elif`, and `else`.
- How to compare values using `==`.
- How to collect numerical input.
- How to perform arithmetic operations.
- How to use conditional logic to select an operation.
- How to display formatted calculation results.

## 3. Project Requirements

The program should:

1. Ask the user to enter two numbers.
2. Display four arithmetic operations.
3. Ask the user to select an operation.
4. Use conditional statements to identify the selected operation.
5. Perform addition, subtraction, multiplication, or division.
6. Display the calculation result.
7. Display a message for an invalid selection.

## 4. Available Operations

| Operation | Symbol | Example |
|---|---|---|
| Addition | `+` | 20 + 5 = 25 |
| Subtraction | `-` | 20 - 5 = 15 |
| Multiplication | `*` | 20 * 5 = 100 |
| Division | `/` | 20 / 5 = 4 |

## 5. Sample Input

```text
Enter first number: 20
Enter second number: 5

Select an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

Enter your choice (1-4): 3
```

## 6. Expected Output

```text
=============================================
          MENU-DRIVEN CALCULATOR
=============================================

Multiplication: 20.0 * 5.0 = 100.0

Thank you for using the calculator!
```

## 7. Concepts Used

### Conditional Statements

- `if` checks the first condition.
- `elif` checks alternative conditions.
- `else` executes when none of the previous conditions match.

### Comparison Operator

The `==` operator checks whether two values are equal.

### Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

### Type Conversion

The `float()` function converts user input into floating-point numbers.

### f-Strings

f-strings display numbers and calculation results in a readable format.

## 8. Practice Challenges

1. Add division-by-zero handling.
2. Display the data types of the inputs and result.
3. Format the result to two decimal places.
4. Add calculation history.
5. Allow repeated calculations using a `while` loop.

## 9. How to Run

Make sure Python is installed and execute:

```bash
python main.py
```

**Note:** Enter a non-zero second number when selecting division. Division-by-zero handling is an additional challenge.

## 10. Project Structure

```text
08A_menu_driven_calculator/
│
├── README.md
└── main.py
```

## 11. Learning Outcome

After completing this project, you should understand how conditional statements control program execution and how to build a simple menu-driven application using Python.

---

**Part of Python From Zero to Projects**

A beginner-friendly, project-based Python learning journey.
