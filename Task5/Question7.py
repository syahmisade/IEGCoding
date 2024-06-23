'''
Problem 7 Harmonic Series:

Write a program that calculates the sum of the first n terms of the harmonic series. 
Take the n as Input.

Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n
'''


def harmonicNum(num):
    harmonic = 0.0
    for i in range(1, num + 1):
        harmonic += 1/i
    return harmonic


num = int(input("Enter the number of terms: "))
result = f"The sum of the first {num} of harmonic series are {harmonicNum(num):.2f}"
print(result)
