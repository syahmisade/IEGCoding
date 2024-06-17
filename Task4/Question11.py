'''
Write a Python program that takes a string as input, which contains numbers separated by commas. 
Convert the string to a list of numbers. Now pick 3 unique numbers from the list whose sum is 100.
'''
x = input("Enter numbers with the usage of commas: ").split(",")
xIntList = list(map(int, x))
xIntSet = set()
found = False

for num in xIntList:
    xIntSet.add(num)
    if num >= 100:
        xIntSet.discard(num)

newList = sorted(list(xIntSet))

for i in range(len(newList)):
    for j in range(i+1, len(newList)):
        for k in range(j+1, len(newList)):
            if newList[i] + newList[j] + newList[k] == 100:
                found = True
                print(
                    f"The 3 unique numbers for sum of 100 are {newList[k]}, {newList[j]}, {newList[i]}")

if found == False:
    print("No unique numbers were found")
