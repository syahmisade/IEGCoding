'''
Problem 6 Perfect Number: Write a program that generates 10 perfect numbers.

Example

6: The divisors of 6 are 1, 2, 3, and 6. 
The sum of its proper divisors (excluding 6 itself) is 1 + 2 + 3 = 6.

28: The divisors of 28 are 1, 2, 4, 7, 14, and 28. 
The sum of its proper divisors (excluding 28 itself) is 1 + 2 + 4 + 7 + 14 = 28.
'''
### Code 1 ##########################################################

# def perfNum(num):  # check if the number is a perfect num
#     sumAll = 1
#     if num <= 1:
#         return False

#     for i in range(2, int(num**2)+1):  # Can use num //2
#         if num % i == 0 and i != num:
#             sumAll += i

#     return sumAll == num


# def loop(num):
#     pNumbers = []
#     n = 2
#     while len(pNumbers) < num:
#         if perfNum(n):
#             pNumbers.append(n)
#         n += 1

#     return pNumbers


# result = f"The first 10 numbers of perfect numbers are {loop(10)}"
# print(result)

### Code 2 ################################################################

def soe(limit):  # set a limit using Sieve Of Eratosthenes algorithm
    sieve = [True] * (limit + 1)  # Create list => keep track of prime number
    sieve[0:2] = [False, False]  # 0 and 1 != prime number

    # iterate up to the square root of the limit
    for currentPrime in range(2, int(limit**0.5)+1):
        if sieve[currentPrime]:  # for each prime number, check again if still prime number
            for multiple in range(currentPrime**2, limit+1, currentPrime):
                sieve[multiple] = False

    primeNum = []

    for p in range(2, limit + 1):
        if sieve[p]:
            primeNum.append(p)
    return primeNum


def gpn(num):  # to generate perfect numbers
    primes = soe(1000000)  # adjust the limit of the prime numbers

    for p in primes:
        perfNum = 2**(p-1)*(2**p - 1)
        yield perfNum
        if num <= 1:
            break
        num -= 1


num = 10
statement = f"The first {10} perfect numbers are :"
print(statement)
for pNum in gpn(num):
    print(pNum)
