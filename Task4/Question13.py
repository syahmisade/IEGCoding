'''
Write a python program to print first 10 terms in a Fibonacci series
'''
xNum = 0
yNum = 1
temp = 0
times = range(10)

print("The first 10 terms in a Fibanacci series are: ")
for count in times:
    print(xNum, end=" ")
    xNum, yNum = yNum, xNum+yNum
