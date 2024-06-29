# Displaying user inputs using multiple return values
# Write a program to display the user entered details and return multiple values.
# Functions Sepcifications:
# def multiVarFunc()
# Input Format:
# First line of input consists of String which is department name.
# Second line of input consists of integer input which is the total number of students
# Third line of input consists of integer input which is the total number of faculty.
# Output Format:
# Display the user inputs.
# Sample Input and Output:
# Enter department name:
# CSE
# Enter the number of total students:
# 60
# Enter the number of total faculties:
# 15
# Details:
# Department:CSE
# Total students:60
# Total faculties:15

def multiVarFunc(department, totalStudents, totalFaculty):
    print(f"Department:{department}")
    print(f"Total students:{totalStudents}")
    print(f"Total faculties:{totalFaculty}")


department = input("Enter department name:\n")
totalStudents = int(input("Enter the number of total students:\n"))
totalFaculty = int(input("Enter the number of total faculties:\n"))
print("Details:")
multiVarFunc(department, totalStudents, totalFaculty)
