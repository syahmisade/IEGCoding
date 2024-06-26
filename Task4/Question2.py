'''
Print first 10 prime numbers using for loop

# much simpler ones (the best logic adalah untuk pakai while loop)
nums = range(2,31)

print("This are the prime number: ")
for num in nums:
    prime = True
    numRange = range(2,num)
    for i in numRange:
        if num % i == 0:
            prime = False
            break
    if prime == True:
        print(f"{num}",end=" ")
'''
nums = range(1, 31)
primeNum = []

for num in nums:
    if num > 1:
        is_prime = True
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
