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

# # Get the number of Adam numbers to generate from user input
# num_items = int(input("Enter the number of Adam numbers to generate: "))

# # Initialize variables
# adam_numbers = []
# num = 1

# # Helper to reverse a number
# def reverse_number(n):
#     return int(str(n)[::-1])

# # Generate the required number of Adam numbers
# while len(adam_numbers) < num_items:
#     # Calculate the square of the number
#     original_square = num ** 2
    
#     # Reverse the number and calculate the square of the reversed number
#     reversed_num = reverse_number(num)
#     reversed_square = reversed_num ** 2
    
#     # Check if the reverse of the square of the number matches the square of the reversed number
#     if reverse_number(original_square) == reversed_square:
#         adam_numbers.append(num)
    
#     # Move to the next number
#     num += 1

# # Print the Adam numbers
# print(f"The first {num_items} Adam numbers are: {adam_numbers}")

# y = 12 # int
# rev = int(str(y)[::-1])
# revsqr = rev**2
# print(rev)
# print(type(rev))
# print(revsqr)

# nums = range(2,31)

# print("This are the prime number: ")
# for num in nums:
#     prime = True
#     numRange = range(2,num)
#     for i in numRange:
#         if num % i == 0:
#             prime = False
#             break
#     if prime == True:
#         print(f"{num}",end=" ")

# x,y,z = input(" ").split(" ")
# print(x,y,z)

# # 10 -> x
# count = 0
# givenNumber = 2
# x = input()
# while count < int(x):
#     isPrime = True
#     divisors = range(2,givenNumber)
#     for i in divisors:
#         if givenNumber % i == 0:
#             isPrime = False
#             break
#     if isPrime == True:
#         print(f"{givenNumber}",end=" ")
#         count += 1
#     givenNumber += 1

# x = int(input(" "))
# alist = []
# fn = 30
# sn = 35
# countF = 0
# countS = 0
# count = 0

# while count<x:

#     if count % 2 == 0:
#         fn += countF
#         alist.append(fn)
#         countF+=8
#     else:
#         sn += countS
#         alist.append(sn)
#         countS+=6

#     count+=1

# for num in alist:
#     print(f"{num}",end=" ")
# n = "123"
# nlist = list(n)
# print(nlist)

# n = input()
# nlist = list(n)
# x=0
# y=0
# if int(n)<10:
#     print("Invalid Input")
# else:
#     for num in nlist:
#         if num == nlist[0]:
#             x += int(num)
#         elif num == nlist[-1]:
#             y += int(num)

#     if x>=y:
#         z = x-y
#     else:
#         z = y-x
#     print(z)

# numpS1 = int(input("Enter the number of people who watched show 1"))
# numaS1 = float(input("Enter the average rating for show 1"))
# numpS2 = int(input("Enter the number of people who watched show 2"))
# numaS2 = float(input("Enter the average rating for show 2"))
# numpS3 = int(input("Enter the number of people who watched show 3"))
# numaS3 = float(input("Enter the average rating for show 3"))

# totalfS1 = numpS1*numaS1
# totalfS2 = numpS2*numaS2
# totalfS3 = numpS3*numaS3

# totalF = totalfS1+totalfS2+totalfS3

# totalP = numpS1+numpS2+numpS3

# totalAveRating = totalF/totalP

# statement = f"The overall average rating for the show is {totalAveRating:.2f}"

# a=(0,1,2,3,4)
# b=slice(0,2)
# print(a[b])

# x = input()
# y = int(input())


# rugby = ["prob","hooker","prob","scrumhalf","standoff","flanker","flanker","number8","inside","outside","winger","blindside"]

# for i in rugby:
#     if i == "flanker":
#         print(f"flanker position in list rugby: {rugby.index(i)}")