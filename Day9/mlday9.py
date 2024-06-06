# Have their on way of addressing the variables to any values
'''
x = 100
y = 100
x = y 
x = 101 #immutable
print(x)
'''

# Mr.Jegan lecture (The location of the object OR id() function)
'''
x = 100
print(id(x)) # To receive the location address of the x in RAM
y =100
print(id(y)) # To receive the location address of the y in RAM (the same location as 100 from x)
# The python gonna scan the contain and assign the variables to the object that already exist
# So, x and y are pointing to the same object in RAM, instead of creating a new object

a = "Hello"
b = "Hello"
print(id(a)) # To receive the location address of the a in RAM
print(id(b)) # To receive the location address of the b in RAM 
'''
# Arithmetic Operation
x = 7
y = 2

print("Addition:",x+y) # print() takes the expression as an argument
print("Subtraction:",x-y)
print("Multiplication:",x*y)
print("Division:",x/y)
print("Quotient:",x//y)
print("Remainder:",x%y)
print("Exponent:", 10**3)
print("What is the maximum number in a 64 bit env:", (2**64)-1)
