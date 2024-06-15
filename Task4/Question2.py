'''
Print first 10 prime numbers using for loop
'''
nums = range(1, 31)
primeNum = []
is_prime = True

for num in nums:
    if num > 1:
        is_prime
        for i in range(2, int(num**0.5) + 1):
            if num % i != 0:
                is_prime = True
            elif num % i == 0:
                is_prime = False
                break
        if is_prime:
            primeNum.append(num)

statement = f"The first 10 prime numbers are {primeNum}"
print(statement)
