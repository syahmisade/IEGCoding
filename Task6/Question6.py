'''
A number is called perfect if the sum of proper divisors of that number is equal to the number. 
For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range
'''
def checkDivisor(i): # Kalau nombor tu pf number atau tak
        sumDiv = 0
        for j in range(1,i):
            if i%j == 0: # 6 == i nombor yang kita nak tgk boleh dibahagikan ke tak == j
                sumDiv += j
        return sumDiv == i

def findPerfectNum(n):
    for k in range(1,n):
        if checkDivisor(k):
            print(k)

num = int(input("Enter max range for perfect number you want: "))
findPerfectNum(num)