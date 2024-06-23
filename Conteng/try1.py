def soe(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]

    for currentPrime in range(2, int(limit**0.5)+1):
        if sieve[currentPrime]:
            for multiple in range(currentPrime**2, limit+1, currentPrime):
                sieve[multiple] = False

    primeNum = []

    for p in range(2, limit + 1):
        if sieve[p]:
            primeNum.append(p)
    return primeNum


def gpn(num):
    primes = soe(1000000)

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
