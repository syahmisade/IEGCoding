'''
Write a python function that takes variable length parameters and returns maximum and minimum number in the parameter numbers.
For example if we call the function: maximumMinimum(10, 20, 30, 40, 50)
The function must return: [10, 50]
'''
def maximumMinimum(*args):
    return [min(args), max(args)]

print(maximumMinimum(10, 20, 30, 40, 50))