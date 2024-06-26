'''
Write a function that takes a number as parameter. 
The function finds the proper divisors of that number and then finds the sum of proper divisors. 
Proper divisors of a number are those numbers by which the number is divisible, except the number itself.
For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18
'''

def divisor(n):
    listDiv = []
    for i in range(1,n):
        if n%i==0:
            listDiv.append(i)
    return listDiv
    
num = int(input("Enter a number to find their divisors: "))
print(divisor(num))
print(f"The sum of the proper divisors: {sum(divisor(num))}")