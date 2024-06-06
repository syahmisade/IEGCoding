'''
Prompts the user to enter two numbers. Swaps the values of the two variables. Prints the values before and after swapping.
'''
var1 = float(input("Enter a number for x: "))
var2 = float(input("Enter a number for y: "))
var3 = 0
var4 = 0

print(f"Value x before swapping: {var1}")
print(f"Value y before swapping: {var2}")

#Swapping easy: var1,var2 = var2,var1

var3 = var1
var4 = var2

var2 = var3
var1 = var4

print(f"Value x after swapping: {var1}")
print(f"Value y after swapping: {var2}")
