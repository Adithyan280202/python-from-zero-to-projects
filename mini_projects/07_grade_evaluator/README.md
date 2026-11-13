# Mini Project 07: Grade Evaluator

## 1. Project Overview

The Grade Evaluator is a beginner-friendly Python project that evaluates a student's academic performance based on marks obtained in five subjects.

The program collects student information and subject marks, calculates the total and percentage, and assigns a grade according to predefined grading criteria.

This project introduces conditional statements in Python.

## 2. Learning Objectives

By completing this project, you will learn:

- How to use conditional statements.
- How to work with `if`, `elif`, and `else`.
- How to use comparison operators.
- How to evaluate multiple conditions.
- How to collect and process numerical input.
- How to calculate total marks and percentages.
- How to display formatted results using f-strings.

## 3. Project Requirements

The program should:

1. Ask for the student's name.
2. Ask for the student's roll number.
3. Collect marks in five subjects.
4. Calculate total marks.
5. Calculate the overall percentage.
6. Evaluate the percentage using conditional statements.
7. Assign an appropriate grade.
8. Display the student's academic result.
9. Display the data types of selected variables.

## 4. Subjects

The program collects marks in the following subjects:

| No. | Subject | Maximum Marks |
|---:|---|---:|
| 1 | English | 100 |
| 2 | Mathematics | 100 |
| 3 | Physics | 100 |
| 4 | Chemistry | 100 |
| 5 | Computer Science | 100 |
| | **Total** | **500** |

## 5. Grading Criteria

| Percentage | Grade |
|---:|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

## 6. Calculation Formulas

### Total Marks

Total = English + Mathematics + Physics + Chemistry + Computer Science

### Percentage

Percentage = (Total Marks / 500) × 100

Since there are five subjects, each carrying 100 marks, the percentage can also be calculated by dividing the total marks by 5.

## 7. Sample Input

```text
Enter student name: Rahul
Enter roll number: 101

English: 85
Mathematics: 95
Physics: 90
Chemistry: 80
Computer Science: 90
```

## 8. Expected Output

```text
=============================================
             STUDENT RESULT
=============================================

Student Name : Rahul
Roll Number  : 101

English          : 85.0
Mathematics      : 95.0
Physics          : 90.0
Chemistry        : 80.0
Computer Science : 90.0

Total Marks : 440.0/500
Percentage  : 88.00%
Grade       : A
```

## 9. Concepts Used

### Conditional Statements

- `if` – Executes a block when a condition is true.
- `elif` – Checks another condition.
- `else` – Executes when all previous conditions are false.

### Comparison Operators

- `>=` Greater than or equal to
- `>` Greater than
- `<=` Less than or equal to
- `<` Less than
- `==` Equal to

### Type Conversion

- `int()` converts input into integers.
- `float()` converts input into floating-point numbers.

### Arithmetic Operators

Addition and division are used to calculate total marks and percentages.

### f-Strings

f-strings display student information and results in a readable format.

## 10. Practice Challenges

Try improving the program by completing these tasks:

1. Add two additional subjects.
2. Find the highest subject mark using `max()`.
3. Find the lowest subject mark using `min()`.
4. Add a separate Pass or Fail status.
5. Display a remark based on the assigned grade.
6. Handle marks outside the valid 0–100 range.
7. Calculate the average mark for each subject.

## 11. How to Run the Project

Make sure Python is installed on your computer.

Open the project folder in VS Code and execute:

```bash
python main.py
```

## 12. Project Structure

```text
07_grade_evaluator/
│
├── README.md
└── main.py
```

## 13. Learning Outcome

After completing this project, you should understand how conditional statements work and how Python can make decisions based on user input and numerical conditions.

---

**Part of Python From Zero to Projects**

A beginner-friendly, project-based Python learning journey.
