'''
Get a number as input and calculate the sum of all numbers from 1 to the given number.
'''
x = int(input("Enter the total number you want: "))
amount = range(1, x+1)
totalAmount = 0

for i in amount:
    totalAmount += i

statement = f"The total amount from 1 until {x} is {totalAmount}"
print(statement)
