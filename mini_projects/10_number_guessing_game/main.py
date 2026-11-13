
# Mini Project 10: Number Guessing Game

print("===================================")
print("       NUMBER GUESSING GAME")
print("===================================")

secret_number = 25
attempts = 0
guess = 0

print("\nI have selected a number between 1 and 50.")
print("Try to guess the correct number!")

while guess != secret_number:

    guess = int(input("\nEnter your guess: "))

    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("\nCongratulations! You guessed the correct number.")
        print("Number of attempts:", attempts)

print("\nThank you for playing!")
