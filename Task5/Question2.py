'''
Write a program that takes an integer input from the user and generates the Collatz sequence for that number. 
The Collatz sequence is defined as follows:

start with a number n. If n is even, the next number is n/2. 
If n is odd, the next number is 3n + 1. Repeat the process until n becomes 1.
'''


def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = 3 * n + 1
        sequence.append(n)
    return sequence


number = int(input("Enter a number for your Collatz sequence: "))

result = collatz_sequence(number)

print(f"The Collatz sequence for your number is: {result}")
