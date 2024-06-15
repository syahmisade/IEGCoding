# x = 3*1**3
# x=22%3
# x=4+3%5
# a = 16
# b = 15
# x=a% b //a
# x = int(43.55+2/2)
# x=2**(3**2)

# print(float (22//3 + 3/3))
# print(x, (2**3)**2,2**3**2)

# x=5
# y=10
# x = x ^ y
# y = x ^ y
# x = x ^ y
# print("X=%d, Y=%d"%(x,y))

# x=5
# k= x+6j
# print("Real part: %d\nImaginary part: %d" % (k.real,k.imag))

# x = "B"
# y = ord(x)
# print(y)

# x = 15
# y0 = oct(x)
# y1 = hex(x)
# print(y0,y1)

# a = 8+4j
# print(a, "is complex number?",isinstance(a,complex))

# x = 60/4
# print(x) #15.0

# x = (2750-800)//130
# print(x) #200

# rev = int(str(12)[::-1])
# print(rev)

# num = str(123)
# y = list(map(int, num))
# print(y)

# n = 152
# digitAmount = len(str(n))
# digits = list(map(int, str(n)))
# armstrongNum = []
# total = 0

# for digit in digits:
#     cubeDigit = digit**digitAmount
#     total += cubeDigit
# print(total)

# if n == total:
#     print(f"{n} is a Armstrong Number")
# else:
#     print(f"{n} is not a Armstrong Number")

####################################################################
# x = 3
# adamNum = []
# lenAN = len(adamNum)
# num = 1

# while x > lenAN:
#     revNum = int(str(num)[::-1])
#     sqrNum = num**2
#     sqrRevNum = revNum**2
#     revSqrRevNum = int(str(sqrRevNum)[::-1])

#     if sqrNum == revSqrRevNum:
#         adamNum.append(num)
    
#     num+=1

# statement = f"The adam numbers are {adamNum}"
# print(statement)

# num_items = int(input("Enter the number of Adam numbers to generate: "))

# Get the number of Adam numbers to generate from user input
num_items = int(input("Enter the number of Adam numbers to generate: "))

# Initialize variables
adam_numbers = []
num = 1

# Helper to reverse a number
def reverse_number(n):
    return int(str(n)[::-1])

# Generate the required number of Adam numbers
while len(adam_numbers) < num_items:
    # Calculate the square of the number
    original_square = num ** 2
    
    # Reverse the number and calculate the square of the reversed number
    reversed_num = reverse_number(num)
    reversed_square = reversed_num ** 2
    
    # Check if the reverse of the square of the number matches the square of the reversed number
    if reverse_number(original_square) == reversed_square:
        adam_numbers.append(num)
    
    # Move to the next number
    num += 1

# Print the Adam numbers
print(f"The first {num_items} Adam numbers are: {adam_numbers}")
