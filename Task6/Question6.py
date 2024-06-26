'''
A number is called perfect if the sum of proper divisors of that number is equal to the number. 
For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range
'''
def perfectNum(n):
    
    def totalDivisor(i):
        sumDiv = 0
        for j in range(1,i):
            if i%j == 0:
                sumDiv += j
        return sumDiv == i
    
    for k in range(1,n):
        if totalDivisor(k):
            print(k)

num = int(input("Enter max range for perfect number you want: "))
perfectNum(num)