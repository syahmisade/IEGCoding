'''
Get number of items as input and generate that many ADAM Numbers
'''
x = int(input("Enter how many Adam numbers you want: "))
y = 100
adamNum = []
nums = range(1, y+1)

for num in nums:
    revNum = int(str(num)[::-1])
    sqrNum = num**2
    sqrRevNum = revNum**2
    revSqrRevNum = int(str(sqrRevNum)[::-1])

    if sqrNum == revSqrRevNum:
        adamNum.append(num)

if len(adamNum) == x:
    

statement = f"The adam numbers are {adamNum}"
print(statement)
