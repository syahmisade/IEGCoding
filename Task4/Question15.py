'''
Write a python program which takes a binary number as input and convert the number to decimal. 
Note: Don't use any builtin functions.
'''
binary_number = input("Enter a binary number: ")
decimal_number = 0

for digit in binary_number:
    decimal_number = decimal_number * 2 + int(digit)

print(f"The decimal number is: {decimal_number}")
