'''
Create a class named Student with a single attribute – marks.
Include a method named check_marks in the Student Class.
This method checks whether the marks is greater than  or equal to 90 and 
if it is greater than or equal to 90, the method returns True.
If the marks is less than 90, a custom Exception named NotEligibleException is raised and 
an appropriate message as shown in the sample output is displayed.
Create a custom Exception class named NotEligibleException.
Create an object of the student class and test the above methods.
Input and Output Format:
Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
Enter marks of student
98
Eligible
Sample Input and Output 2:
Enter marks of student
56
Inside Except Block : Not Eligible
'''


class NotEligibleException(Exception):
    pass


class Student:
    def __init__(self, marks):
        self.marks = marks

    def check_marks(self):
        if self.marks >= 90:
            return True
        else:
            raise NotEligibleException("Not Eligible")


try:
    marks = int(input("Enter marks of student\n"))
    s = Student(marks)

    if s.check_marks() == True:
        print("Eligible")
except NotEligibleException as e:
    print("Inside Except Block :", e)
