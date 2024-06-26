'''
Write a simple python function that takes a number as parameter and returns the prime factors of that number. 
Prime Factorization is finding which prime numbers multiply together to make the original number.
Example: prime factors of 56 - 2, 2, 2, 7
'''

def primeFactors(x):
    factors = []
    prime = 2
    
    while x>1:
        while x%prime == 0:
            factors.append(prime)
            x //= prime
        prime+=1
    
    return factors

num = int(input("Enter a number to find their prime factors: "))
print(primeFactors(num))