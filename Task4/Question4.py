'''
Get number of items as input and generate that many Armstrong Numbers
'''
x = int(input("Enter how many Armstrong numbers you want: "))

nums = range(1, x+1)
armstrongNum = []

for num in nums:
    digitAmount = len(str(num))
    digits = list(map(int, str(num)))
    total = 0
    for digit in digits:
        cubeDigit = digit**digitAmount
        total += cubeDigit

    if num == total:
        armstrongNum.append(num)

statement = f"The armstrong numbers are {armstrongNum}"
print(statement)
