'''
Get number of items as input and generate that many ADAM Numbers
'''
x = int(input("Enter how many Adam numbers you want: "))
y = 1
adamNum = []
# lenAN = len(adamNum)

while x > len(adamNum):
    revNum = int(str(y)[::-1])
    sqrNum = y**2
    sqrRevNum = revNum**2
    revSqrRevNum = int(str(sqrRevNum)[::-1])

    if sqrNum == revSqrRevNum:
        adamNum.append(y)

    y += 1


statement = f"The {x} adam numbers are {adamNum}"
print(statement)
