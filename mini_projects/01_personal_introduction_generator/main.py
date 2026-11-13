
# Mini Project 01
# Personal Introduction Generator

print("Welcome to the Personal Introduction Generator!")
print()

# Collect user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
place = input("Enter your place: ")
education = input("Enter your education: ")
hobby = input("Enter your hobby: ")

# Display data types
print("\n" + "=" * 40)
print("         DATA TYPES")
print("=" * 40)

print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))
print("Place:", type(place))
print("Education:", type(education))
print("Hobby:", type(hobby))

# Display personal introduction
print("\n" + "=" * 40)
print("       PERSONAL INTRODUCTION")
print("=" * 40)

print(f"Hello! My name is {name}.")
print(f"I am {age} years old.")
print(f"My height is {height} metres.")
print(f"I am from {place}.")
print(f"My education is {education}.")
print(f"My favourite hobby is {hobby}.")

print("\nThank you for using this program!")
