# Create a class named Person with the following 2 public attributes.
# name
# age
# Include a constructor:
#            __init__(self,name, age)
# Create an object of class Person to test the above class.
# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.
# Sample Input and Output:
# [All text in bold corresponds to input and the rest corresponds to output]
# Enter name
# Mahirl
# Enter age
# 10
# Person Details
# Mahirl
# 10

# Person.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# from Person import Person
p = Person(input("Enter name\n"), int(input("Enter age\n")))
print("Person Details")
print(p.name)
print(p.age)