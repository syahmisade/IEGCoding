'''
Write a program that takes two integers from the user and calculates their 
greatest common divisor (GCD) using the Euclidean algorithm.

You can refer this Link

https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
'''


def gcd(a, b):

    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


x = int(input("Enter a number for A: "))
y = int(input("Enter a number for B: "))

result = gcd(x, y)

print(f"GCD is {result}")
