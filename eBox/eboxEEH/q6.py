'''
A vote is a formal expression of an individual's choice in voting. Government elected by its citizens, 
and voting is an important right in our society. Log sabha election in Delhi held in October 2016. 
And as we know that voting age 18, is a minimum age established by law that a 
person must attain before they become eligible to vote.
Thus, write a program to get the name and age of the people who all are eligible for voting.
Note:
If people is eligible to vote only after 18 and above.
This program may generate:
1. InvalidAgeRange Custom Exception when the People's age is below 18
 Use exception handling mechanisms to handle these exceptions
Create a class called CustomException which extends Exception and 
it includes constructor to initialize the message.
Use appropriate exception handling mechanisms to handle these exceptions  
Input and Output Format:
Refer sample input and output for formatting specifications.
Note: All text in bold corresponds to input and the rest corresponds to output.
Sample  Input/Output 1:
Enter the Name
naveen
Enter the age
25
Voter name: naveen
Voter age: 25
Sample  Input/Output 2:
Enter the Name
shilpa
Enter the age
12
CustomException: InvalidAgeRangeException
'''


class CustomException(Exception):
    pass


def vote(name, age):
    pass


name = input("Enter the Name:\n")
age = int(input("Enter the age:\n"))
vote(name, age)
