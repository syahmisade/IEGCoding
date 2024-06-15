'''
Write a python program that takes few numbers as command line argument. 
Use a loop to display all elements. Use another loop to display all elements in the even position. 
Use another loop to display all elements in the odd position.
'''
import sys

cmdarg = sys.argv[1:]

print("The total elements are:")
for element in cmdarg:
    print(element)

print("The even position from the elements are: ")
for x in range(0, len(cmdarg), 2):
    print(cmdarg[x])

print("The odd position from the elements are: ")
for y in range(1, len(cmdarg), 2):
    print(cmdarg[y])
