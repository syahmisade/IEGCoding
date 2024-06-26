'''
Write a python function that takes a number as parameter and prints the multiplication table of that number
'''

def multiTable(x):
    for i in range(1,13):
        multi = i*x
        print(f"{i} x {x} = {multi}")

x = int(input("Enter a number for multiple table: "))
multiTable(x)