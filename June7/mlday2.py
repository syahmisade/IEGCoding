'''
By Mr.Jagen lecture
'''
# Assignment Operators
x = 100
x += 1 # x = x + 1

# y = mx + c
# y = x**2 + 2 * x + 3

x += 2 # x = x + 2
x += 5 # x = x + 5
x += x + 1 # x = x + x + 1
# print(x) # x = 108 + 109 = 217

x -= 1 # x = x - 1
'''
x (Ops)= 1 : x = x (Ops) 1

Examples:
x += 1 : x = x + 1
x -= 1 : x = x - 1
x *= 1 : x = x * 1
x /= 1 : x = x / 1
x //= 1 : x = x // 1
x %= 1 : x = x % 1
'''

###############################################################################
givenNumber = 97531
# result = givenNumber % 10 # 1
result = 0

# givenNumber = givenNumber // 10 # 9753
givenNumber //= 10 # 9753 (Try to write code more like this!)
result = result * 10 + (givenNumber % 10)

print(givenNumber, result)

###############################################################################
x,y = 101,102
x,y = 101 + 1,102 + 2
x,y = x + 1,y + 1
print(x,y)

# unvalid in Python: x,y = 105

###############################################################################
z = 0 # Numeric Initialization 
z = "" # String Initialization
z = None # None type (Third keyword for Boolean)

###############################################################################
'''
Definete Statement
(Truth table)

and
or
xor
and more

'''
varA = 21
varB = 14
varC = 7 

print(varA>varB and varA>varC) #varA is the greatest number
print(varC < varA and varC < varB) #varC is the smallest
print(varB>varC and varB<varA) 
print((varB<varA)or(varB>varC))

###############################################################################
'''
Negation operator

not(Argument)

'''
