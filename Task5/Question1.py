'''
Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, 
and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
'''


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


x = range(1, 101)

for i in x:
    print(fizzbuzz(i))
