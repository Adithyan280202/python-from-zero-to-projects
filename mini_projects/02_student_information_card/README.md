# Mini Project 02: Student Information Card

## 1. Project Overview

The Student Information Card is a beginner-friendly Python project that collects personal and academic details from a student and displays them in a properly formatted information card.

This project helps learners understand how to work with different Python data types, accept user input, perform type conversion, and format output.

## 2. Learning Objectives

By completing this project, you will learn:

- How to create and use variables.
- How to collect information using `input()`.
- How to work with strings, integers, and floating-point numbers.
- How to convert input using `int()` and `float()`.
- How to identify variable data types using `type()`.
- How to display formatted information using f-strings.
- How to organize program output.

## 3. Information to Collect

The program should collect the following details:

| Information | Data Type |
|---|---|
| Student Name | String (`str`) |
| Roll Number | Integer (`int`) |
| Age | Integer (`int`) |
| Height in metres | Float (`float`) |
| CGPA | Float (`float`) |
| Department | String (`str`) |
| College Name | String (`str`) |
| Attendance Percentage | Float (`float`) |

## 4. Program Workflow

1. Display a welcome message.
2. Ask the student to enter personal information.
3. Ask for academic details.
4. Convert numerical inputs into the appropriate data types.
5. Display the data type of each variable.
6. Generate a formatted Student Information Card.
7. Display all collected information.

## 5. Sample Input

```text
Enter student name: Rahul
Enter roll number: 101
Enter age: 21
Enter height in metres: 1.75
Enter CGPA: 8.5
Enter department: Computer Science
Enter college name: ABC Engineering College
Enter attendance percentage: 92.5
```

## 6. Expected Output

```text
=============================================
          STUDENT INFORMATION CARD
=============================================

Student Name       : Rahul
Roll Number        : 101
Age                : 21
Height             : 1.75 metres
CGPA               : 8.5
Department         : Computer Science
College            : ABC Engineering College
Attendance         : 92.5%

=============================================
```

The program should also display the data types of all collected variables before printing the information card.

## 7. Concepts Used

### Variables
Variables store the personal and academic information entered by the student.

### Input Function
The `input()` function collects information from the user.

### Data Types
- `str` – Stores text.
- `int` – Stores whole numbers.
- `float` – Stores decimal numbers.

### Type Conversion
- `int()` converts input into