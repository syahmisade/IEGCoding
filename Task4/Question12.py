'''
Write a Python program to get 2 positive numbers as input and
multiply them without using the '*' operator.
'''
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
result = 0

if x < 0 and y < 0:
    print("Please enter a positive number")
else:
    for times in range(y):
        result += x
    print(f"The multiplication of {x} and {y} is {result}")
