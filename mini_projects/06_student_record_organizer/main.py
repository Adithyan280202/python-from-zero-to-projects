
# Mini Project 06
# Student Record Organizer

print("=" * 45)
print("        STUDENT RECORD ORGANIZER")
print("=" * 45)

# Collect information for three students
name1 = input("Enter Student 1 name: ")
roll1 = int(input("Enter Student 1 roll number: "))
mark1 = float(input("Enter Student 1 mark: "))

print()

name2 = input("Enter Student 2 name: ")
roll2 = int(input("Enter Student 2 roll number: "))
mark2 = float(input("Enter Student 2 mark: "))

print()

name3 = input("Enter Student 3 name: ")
roll3 = int(input("Enter Student 3 roll number: "))
mark3 = float(input("Enter Student 3 mark: "))

# Store names in a list
student_names = [name1, name2, name3]

# Store roll numbers in a tuple
roll_numbers = (roll1, roll2, roll3)

# Store unique marks in a set
student_marks = {mark1, mark2, mark3}

# Store complete records in a dictionary
student_records = {
    roll1: {"name": name1, "mark": mark1},
    roll2: {"name": name2, "mark": mark2},
    roll3: {"name": name3, "mark": mark3}
}

# Calculate total and average marks
total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

# Display data types
print("\n" + "=" * 45)
print("             DATA TYPES")
print("=" * 45)

print("Student Names:", type(student_names))
print("Roll Numbers:", type(roll_numbers))
print("Student Marks:", type(student_marks))
print("Student Records:", type(student_records))

# Display student records
print("\n" + "=" * 45)
print("             STUDENT RECORDS")
print("=" * 45)

print("Student Names:", student_names)
print("Roll Numbers:", roll_numbers)
print("Unique Marks:", student_marks)
print("Complete Records:", student_records)

# Display individual student details
print("\n" + "=" * 45)
print("           STUDENT DETAILS")
print("=" * 45)

print(f"Student 1: {name1} | Roll: {roll1} | Mark: {mark1}")
print(f"Student 2: {name2} | Roll: {roll2} | Mark: {mark2}")
print(f"Student 3: {name3} | Roll: {roll3} | Mark: {mark3}")

# Display statistics
print("\n" + "=" * 45)
print("          MARK STATISTICS")
print("=" * 45)

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

print("=" * 45)
print("       RECORDS ORGANIZED SUCCESSFULLY!")
print("=" * 45)
