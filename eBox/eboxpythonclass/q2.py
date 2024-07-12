# Create a class named Person with the following 2 private attributes.
# __name
# __age
# Include a constructor:
# __init__(self,name, age)
# Include a method:
# __str__(self)
# This method returns a string corresponding to person details in the format specified in the sample output.
# Include a @classmethod:
# from_string(cls, person_str)
# This method creates and returns an object of Person class from a string. This method accepts a class variable and a string.
# String contains the values for name and age in a comma separated format.
# Create objects of class Person to test the above class.

# Person.py
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split(',')
        return cls(name, int(age))
    
    def __str__(self):
        return f"Person Details\n{self.__name}\n{self.__age}"
    
# Main.py
# from Person import Person
print("Creating object using __init__ method")
person_name = input("Enter name\n")
person_age = input("Enter age\n")
person1 = Person(person_name, person_age)
print("Person Details")
print(person1)
print("\n")

print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)