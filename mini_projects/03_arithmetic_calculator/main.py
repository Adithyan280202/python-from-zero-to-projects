
# Mini Project 03
# Simple Arithmetic Calculator
# Without Conditional Statements

print("=" * 45)
print("          SIMPLE CALCULATOR")
print("=" * 45)

# Get two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display data types
print("\n" + "=" * 45)
print("              DATA TYPES")
print("=" * 45)

print("First number:", type(num1))
print("Second number:", type(num2))
print("Addition:", type(addition))
print("Subtraction:", type(subtraction))
print("Multiplication:", type(multiplication))
print("Division:", type(division))

# Display calculation results
print("\n" + "=" * 45)
print("          CALCULATION RESULTS")
print("=" * 45)

print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")

print("\nThank you for using the calculator!")
