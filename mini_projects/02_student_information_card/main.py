
# Mini Project 02
# Student Information Card

print("=" * 45)
print("       STUDENT INFORMATION SYSTEM")
print("=" * 45)

# Collect student information
name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))
age = int(input("Enter age: "))
height = float(input("Enter height in metres: "))
cgpa = float(input("Enter CGPA: "))
department = input("Enter department: ")
college = input("Enter college name: ")
attendance = float(input("Enter attendance percentage: "))

# Display data types
print("\n" + "=" * 45)
print("             DATA TYPES")
print("=" * 45)

print("Name:", type(name))
print("Roll Number:", type(roll_number))
print("Age:", type(age))
print("Height:", type(height))
print("CGPA:", type(cgpa))
print("Department:", type(department))
print("College:", type(college))
print("Attendance:", type(attendance))

# Display student information card
print("\n" + "=" * 45)
print("          STUDENT INFORMATION CARD")
print("=" * 45)

print(f"Student Name       : {name}")
print(f"Roll Number        : {roll_number}")
print(f"Age                : {age}")
print(f"Height             : {height} metres")
print(f"CGPA               : {cgpa}")
print(f"Department         : {department}")
print(f"College            : {college}")
print(f"Attendance         : {attendance}%")

print("=" * 45)
print("       END OF STUDENT INFORMATION")
print("=" * 45)
