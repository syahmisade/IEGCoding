# contoh = "awdsdaef dawdsdfa dawdasda "
# x = set(contoh)
# x.remove(' ')
# print(x)

# x = ["what","is","5"]
# xstr = str(x)
# print(xstr)

# example = "what is 5?".split()
# x,y,z = "what","is","?"
# contoh = list(example)
# if x and y and z in contoh:
#     contoh.remove(x)
#     contoh.remove(y)
#     contoh.remove(z)
# else:
#     print("This machine does not understand the statement")

# print(contoh)

# contoh 1
def case_1():
    return "Case 1"

def case_2():
    return "Case 2"

def case_default():
    return "Default case"

dispatch = {
    1: case_1,
    2: case_2
}

x = int(input("Enter a number to determine the case: "))
result = dispatch.get(x, case_default)()
print(result)

# Ternary conditional operator 2
result = "Greater" if x > 5 else "Smaller or Equal"
print(result)

# Other ways 3
def condition_1():
    return "Condition 1"

def condition_2():
    return "Condition 2"

def default():
    return "Default"

conditions = {
    True: condition_1,
    False: condition_2
}

x = 10
result = conditions.get(x > 5, default)()
print(result)

# Other ways 4
x = 10
result = (x > 5 and "Greater") or "Smaller or Equal"
print(result)

# Other ways 5
numbers = [1, 2, 3, 4, 5]
result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(result)

# Other ways 5
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Cannot divide by zero"


