'''
Prompts the user to enter two numbers. Stores these numbers in two variables. 
Performs and prints the results of addition, subtraction, multiplication, and division of these two numbers.
'''
var1 = int(input("Choose a number for first variables: "))
var2 = int(input("Choose a number for second variables: "))

addition = var1 + var2
subtraction = var1 - var2
multiplication = var1 * var2
division = var1 / var2

print(f"The result of addition: {addition}")
print(f"The result of substaction: {subtraction}")
print(f"The result of multiplication: {multiplication}")
print(f"The result of division: {division}")