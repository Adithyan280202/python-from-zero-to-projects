
# Mini Project 07
# Grade Evaluator

print("=" * 45)
print("             GRADE EVALUATOR")
print("=" * 45)

# Collect student information
student_name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))

# Collect subject marks
print("\nEnter marks out of 100")

english = float(input("English: "))
mathematics = float(input("Mathematics: "))
physics = float(input("Physics: "))
chemistry = float(input("Chemistry: "))
computer = float(input("Computer Science: "))

# Calculate total and percentage
total = english + mathematics + physics + chemistry + computer
percentage = total / 5

# Grade evaluation
if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 50:
    grade = "D"

else:
    grade = "F"

# Display data types
print("\n" + "=" * 45)
print("              DATA TYPES")
print("=" * 45)

print("Student Name:", type(student_name))
print("Roll Number:", type(roll_number))
print("Total Marks:", type(total))
print("Percentage:", type(percentage))
print("Grade:", type(grade))

# Display student result
print("\n" + "=" * 45)
print("             STUDENT RESULT")
print("=" * 45)

print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")

print("-" * 45)
print(f"English          : {english}")
print(f"Mathematics      : {mathematics}")
print(f"Physics          : {physics}")
print(f"Chemistry        : {chemistry}")
print(f"Computer Science : {computer}")

print("-" * 45)
print(f"Total Marks : {total}/500")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")

print("=" * 45)
print("          RESULT GENERATED!")
print("=" * 45)
