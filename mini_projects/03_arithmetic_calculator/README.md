# Mini Project 03: Simple Arithmetic Calculator

## 1. Project Overview

Build a simple Python calculator that accepts two numbers and performs four basic arithmetic operations: addition, subtraction, multiplication, and division.

This project introduces variables, user input, type conversion, data types, and arithmetic operators.

## 2. Learning Objectives

- Create and use variables.
- Collect numerical input using `input()`.
- Convert input into floating-point numbers using `float()`.
- Perform basic arithmetic operations.
- Identify data types using `type()`.
- Display results using f-strings.

## 3. Project Requirements

The program should:

1. Ask the user to enter two numbers.
2. Convert both inputs into floating-point numbers.
3. Calculate addition, subtraction, multiplication, and division.
4. Display the data types of the inputs and results.
5. Display all calculation results.

**Important:** Do not use conditional statements (`if`, `elif`, `else`) in this project.

## 4. Arithmetic Operations

| Operation | Operator | Example |
|---|---|---|
| Addition | `+` | 20 + 5 = 25 |
| Subtraction | `-` | 20 - 5 = 15 |
| Multiplication | `*` | 20 * 5 = 100 |
| Division | `/` | 20 / 5 = 4 |

## 5. Sample Input

```text
Enter the first number: 20
Enter the second number: 5
```

## 6. Expected Output

```text
=============================================
          SIMPLE CALCULATOR
=============================================

First number: <class 'float'>
Second number: <class 'float'>
Addition: <class 'float'>
Subtraction: <class 'float'>
Multiplication: <class 'float'>
Division: <class 'float'>

=============================================
          CALCULATION RESULTS
=============================================

Addition       : 25.0
Subtraction    : 15.0
Multiplication : 100.0
Division       : 4.0

Thank you for using the calculator!
```

## 7. Concepts Used

- Variables
- `input()` and `print()`
- `float()` type conversion
- `type()` function
- Arithmetic operators
- f-strings

## 8. Practice Challenges

1. Add modulus (`%`) operation.
2. Add exponentiation (`**`).
3. Calculate the average of the two numbers.
4. Display results rounded to two decimal places.
5. Ask for a third number and perform calculations with it.
6. Display the square of each input number.

## 9. How to Run

Make sure Python is installed and run:

```bash
python main.py
```

**Note:** Enter a non-zero second number because division by zero causes a runtime error.

## 10. Project Structure

```text
03_arithmetic_calculator/
│
├── README.md
└── main.py
```

## 11. Learning Outcome

After completing this project, you should be able to collect numerical input, perform arithmetic calculations, identify data types, and display formatted results using Python.

---

**Part of Python From Zero to Projects**

A beginner-friendly, project-based Python learning journey.
