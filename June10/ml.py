'''
Bitwise Operation (This only apply for binary)
'''

ownerpermission = 0b111 # 0b == represent binary number from basic decimal number
print(ownerpermission)

filepermission = 0b111101001
print(filepermission)
#owner == Read,Write,Execute
#group == Read,Execute
#other == Execute

'''
In categorical data, CONVERT them to numbers which the machine can understand.
This is called "feature engineering"

Examples:
Gender representation:
- Male == 10
- Female == 01
Race representation:
- Malay == 1000
- Chinese == 0100

'''
# The bit extraction can be using bitwise and operator ***Binary always start dari kanan
mask = 0b000111000
x = filepermission & mask
print("{0:b}".format(x >> 3)) # >> == movekan nombor sekian2 ke kanan #decimal
print(x >> 3) #decimal