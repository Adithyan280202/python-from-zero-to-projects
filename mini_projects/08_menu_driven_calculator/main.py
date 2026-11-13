
# Mini Project 08A
# Menu-Driven Calculator

print("=" * 45)
print("          MENU-DRIVEN CALCULATOR")
print("=" * 45)

# Get two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation menu
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice (1-4): ")

# Perform calculation
if choice == "1":
    result = num1 + num2
    print(f"\nAddition: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"\nSubtraction: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"\nMultiplication: {num1} * {num2} = {result}")

elif choice == "4":
    result = num1 / num2
    print(f"\nDivision: {num1} / {num2} = {result}")

else:
    print("\nInvalid choice! Please select 1, 2, 3, or 4.")

print("\nThank you for using the calculator!")
