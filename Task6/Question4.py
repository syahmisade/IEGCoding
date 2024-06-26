'''
Write a function that inputs a number and returns the product of digits of that number.
'''

def productdDigit(num):
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    return product
    

num = int(input("Enter a number to search the product: "))
print(productdDigit(num))