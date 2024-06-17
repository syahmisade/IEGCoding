'''
Write a python program which takes a number as input and convert the number to binary.
Note: Don't use any builtin functions.
'''
number = int(input("Enter a number: "))

binary = ''

if number == 0:
    binary = '0'

while number > 0:
    binary = str(number % 2) + binary
    number = number // 2

print(f"The binary representation is: {binary}")
