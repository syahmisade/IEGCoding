'''
Write a program to print the following pattern using a loop
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
amount = 5
lines = range(1, amount+1)
newLine = " "

for x in lines:
    for y in range(1, x+1):
        print(y, end=" ")
    print(newLine)
