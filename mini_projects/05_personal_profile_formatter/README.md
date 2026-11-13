# Mini Project 05: Personal Profile Formatter

## 1. Project Overview

The Personal Profile Formatter is a beginner-friendly Python project that collects basic personal information from a user and generates a neatly formatted personal profile.

The program accepts the user's name, email address, place, and profession. It cleans unnecessary spaces, formats text, generates a username, and displays the final profile.

This project introduces practical Python string manipulation.

## 2. Learning Objectives

By completing this project, you will learn:

- How to collect information using `input()`.
- How to store information using variables.
- How to manipulate strings using built-in methods.
- How to remove unnecessary spaces.
- How to convert text into uppercase, lowercase, and title case.
- How to replace characters in strings.
- How to calculate string length using `len()`.
- How to identify data types using `type()`.
- How to display formatted output using f-strings.

## 3. Project Requirements

The program should:

1. Ask for the user's full name.
2. Ask for the email address.
3. Ask for the user's place.
4. Ask for the user's profession.
5. Remove unnecessary spaces from the inputs.
6. Convert the name into title case.
7. Generate a username using the name.
8. Convert the email address into lowercase.
9. Format the place and profession.
10. Calculate the length of the name and email.
11. Display the data types of selected variables.
12. Generate a formatted personal profile.

**Important:** Complete this project without conditional statements or loops.

## 4. Information to Collect

| Information | Data Type |
|---|---|
| Full Name | String (`str`) |
| Email Address | String (`str`) |
| Place | String (`str`) |
| Profession | String (`str`) |

## 5. String Methods Used

| Method | Purpose |
|---|---|
| `strip()` | Removes spaces at the beginning and end |
| `title()` | Converts text into title case |
| `lower()` | Converts text into lowercase |
| `upper()` | Converts text into uppercase |
| `replace()` | Replaces characters or text |
| `len()` | Returns the number of characters |

## 6. Sample Input

```text
Enter your full name:    rahul kumar
Enter your email address: RAHUL@GMAIL.COM
Enter your place: munnar
Enter your profession: software developer
```

## 7. Expected Output

```text
=============================================
              PERSONAL PROFILE
=============================================

Full Name    : Rahul Kumar
Username     : rahul.kumar
Email        : rahul@gmail.com
Place        : Munnar
Profession   : Software Developer

---------------------------------------------
Name Length  : 11 characters
Email Length : 16 characters

=============================================
```

The program should also display the data types of the collected and generated variables.

## 8. Concepts Used

### Variables
Variables store the personal information entered by the user.

### Input Function
The `input()` function collects information from the keyboard.

### String Manipulation
Python provides built-in methods to modify and format strings.

### String Length
The `len()` function calculates the number of characters in a string.

### String Replacement
The `replace()` method replaces spaces with dots to generate a username.

### Type Function
The `type()` function identifies the data type of a variable.

### f-Strings
f-strings allow variables to be displayed in formatted output.

## 9. Practice Challenges

Try improving the program by completing these tasks:

1. Generate a username using underscores instead of dots.
2. Display the first character of the user's name.
3. Display the last character of the email address.
4. Count the number of words in the full name.
5. Ask for the user's favourite programming language.
6. Generate another username using the name and a number entered by the user.
7. Display the name in uppercase and lowercase.

## 10. How to Run the Project

Make sure Python is installed on your computer.

Open the project folder in VS Code and run:

```bash
python main.py
```

## 11. Project Structure

```text
05_personal_profile_formatter/
│
├── README.md
└── main.py
```

## 12. Learning Outcome

After completing this project, you should be able to collect personal information, manipulate strings, generate usernames, format text, calculate string lengths, and display structured information using Python.

---

**Part of Python From Zero to Projects**

A beginner-friendly, project-based Python learning journey.
