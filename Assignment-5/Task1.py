# Task 1: Create a Dictionary of Student Marks

# Create dictionary of student marks
student_marks = {
    "Dhruvil": 87,
    "Abhay": 92,
    "Tushar": 78,
    "Jay": 85,
    "Kartik": 90
}

# Ask user for input
name = input("Enter student name: ")

# Retrieve marks with error handling
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found in the records.")
