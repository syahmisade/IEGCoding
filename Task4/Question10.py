'''
Write a Python program that takes a string as input, 
which contains numbers separated by commas. 
Convert the string to a list of numbers and determine whether 
all the numbers are different from each other.
'''
x = input("Enter numbers with the usage of commas: ").split(",")
xIntList = list(map(int, x))
countUnique = set()

for num in xIntList:
    if num in countUnique:
        print("Not all elements are unique")
        break
    countUnique.add(num)
else:
    print("All elements are unique")
