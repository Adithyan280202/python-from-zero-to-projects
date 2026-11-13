
# Mini Project 10: Number Guessing Game

## Project Overview

The Number Guessing Game is a simple interactive Python game where the user tries to guess a secret number selected by the program.

The program gives hints to the user by displaying whether the guessed number is too high or too low.

The game continues until the user guesses the correct number.

## Objectives

- Understand conditional statements.
- Practise while loops.
- Use comparison operators.
- Track the number of attempts.
- Build an interactive Python program.

## Requirements

- Python 3.x
- VS Code or any Python code editor.

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the command:

```bash
python main.py
```

## Sample Input

```text
Enter your guess: 15
Enter your guess: 35
Enter your guess: 25
```

## Sample Output

```text
I have selected a number between 1 and 50.
Try to guess the correct number!

Too low! Try a bigger number.

Too high! Try a smaller number.

Congratulations! You guessed the correct number.
Number of attempts: 3

Thank you for playing!
```

## Concepts Used

### 1. Variables

Used to store the secret number, user's guess and number of attempts.

### 2. While Loop

Repeats the guessing process until the correct number is entered.

### 3. Conditional Statements

Uses if, elif and else to compare the user's guess with the secret number.

### 4. Comparison Operators

Uses !=, < and > to compare numbers.

### 5. Increment Operator

The attempts variable is increased after every guess.

## Practice Challenges

1. Change the secret number.
2. Change the guessing range to 1–100.
3. Display the number of attempts after every guess.
4. Give the user only 5 attempts.
5. Allow the user to play another round.

## Learning Outcomes

After completing this project, you will understand how to:

- Use while loops in practical applications.
- Apply conditional statements.
- Compare numerical values.
- Track user attempts.
- Develop simple interactive games.

---

**Part of the Python From Zero to Projects learning series.**
