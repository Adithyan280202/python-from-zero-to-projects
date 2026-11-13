# Mini Project 01: Personal Introduction Generator

## 1. Project Overview

The Personal Introduction Generator is a beginner-friendly Python project that collects basic information from the user, identifies the data types of the collected values, and generates a formatted personal introduction.

This project helps beginners understand how Python variables store different types of information.

## 2. Learning Objectives

By completing this project, you will learn:

- How to declare and use variables.
- How to collect information using `input()`.
- How to work with strings, integers, and floating-point numbers.
- How to convert input data using `int()` and `float()`.
- How to identify data types using `type()`.
- How to display formatted output using f-strings.

## 3. Requirements

The program should collect the following information:

| Input | Data Type |
|---|---|
| Full Name | String (`str`) |
| Age | Integer (`int`) |
| Height in metres | Float (`float`) |
| Place | String (`str`) |
| Education | String (`str`) |
| Favourite Hobby | String (`str`) |

## 4. Program Workflow

1. Display a welcome message.
2. Ask the user to enter their personal information.
3. Convert age into an integer.
4. Convert height into a floating-point number.
5. Display the data type of every variable.
6. Generate and display the personal introduction.
7. Display a thank-you message.

## 5. Sample Input

```text
Enter your name: Adithyan
Enter your age: 24
Enter your height in metres: 1.80
Enter your place: Munnar
Enter your education: BTech EEE
Enter your hobby: Robotics
```

## 6. Expected Output

```text
========================================
              DATA TYPES
========================================

Name: <class 'str'>
Age: <class 'int'>
Height: <class 'float'>
Place: <class 'str'>
Education: <class 'str'>
Hobby: <class 'str'>

========================================
       PERSONAL INTRODUCTION
========================================

Hello! My name is Adithyan.
I am 24 years old.
My height is 1.8 metres.
I am from Munnar.
My education is BTech EEE.
My favourite hobby is Robotics.

Thank you for using this program!
```

## 7. Concepts Used

### Variables
Variables are used to store the information entered by the user.

### Input Function
The `input()` function collects information from the keyboard.

### Data Types
Python supports different data types:

- `str` – Stores text.
- `int` – Stores whole numbers.
- `float` – Stores decimal numbers.

### Type Conversion
The `int()` and `float()` functions convert input strings into numeric values.

### Type Function
The `type()` function identifies the data type of a variable.

### f-Strings
f-strings allow variables to be inserted directly into formatted text.

## 8. Practice Challenges

Try improving the program by completing these additional tasks:

1. Ask the user for their favourite programming language.
2. Ask for their dream job.
3. Collect their college or school name.
4. Display all information in a more attractive format.
5. Add the current year of study.
6. Display the user's height in centimetres as well as metres.

## 9. How to Run the Project

Make sure Python is installed on your computer.

Open the project folder in VS Code and run:

```bash
python main.py
```

## 10. Project Structure

```text
01_personal_introduction_generator/
│
├── README.md
└── main.py
```

## 11. Learning Outcome

After completing this project, you should be able to collect user input, store information in variables, work with basic Python data types, perform type conversion, and generate formatted output.

---

**Part of Python From Zero to Projects**

Created for beginners who want to learn Python through practical programming.
