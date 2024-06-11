'''
Bitwise Operation (This only apply for binary)
'''
line = "="*50

ownerpermission = 0b111 # 0b == represent binary number from basic decimal number
oPBit = "{0:b}".format(ownerpermission)
filepermission = 0b111101001
fPBit = "{0:b}".format(filepermission)

print(f"{ownerpermission} is the owner permission")
print(f"{oPBit} is the owner permission in binary format")
print(line)
print(f"{filepermission} is the file permission")
print(f"{fPBit} is the file permission in binary format")
#owner == Read,Write,Execute
#group == Read,Execute
#other == Execute
print(line)

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
maskBinary = "{0:b}".format(mask)

print(f"The mask value is: {mask} in decimal and {maskBinary} in binary")

print(line)

#AND Binary ==================================================================================
andBit = (filepermission & mask) >> 3 # >> == movekan nombor sekian2 ke kanan #decimal
andBitBinary = "{0:b}".format(andBit)

print("AND OPERATION")
print(f"The binary for AND operation is {andBitBinary}") 
print(f"The decimal for AND operation is {andBit}") #decimal

print(line)

#OR Operation =================================================================================
orBit = filepermission | mask
orBitBinary = "{0:b}".format(orBit)

print("OR OPERATION")
print(f"The binary for OR operation is {orBitBinary}") 
print(f"The decimal for OR operation is {orBit}") #decimal

print(line)

'''
We can create a key based on ASCII character
This is more related on encrypted data or information
'''
# XOR Operation ===============================================================================
message = 0b10100101
key = 0b11001100
encrypted_message = message ^ key
decrypted_message = encrypted_message ^ key

print("XOR OPERATION") 
print(f"The message is {message} and thebinary format is {bin(message)}")
print(f"The key is {key} and the binary format is {bin(key)}")
print(f"The encrypted message is {encrypted_message} in decimal and {bin(encrypted_message)} in binary")
print(f"The decrypted message is {decrypted_message} in decimal and {bin(decrypted_message)} in binary")

print(line)

'''
Complement
5 == 0101
1s complement == 1010
2s complement == 1011 (1s complement + 1)
Unary Negative == (-)
Unary Positive == (+)
'''
number = 5
onesComplement = ~number
twosComplement = ~number + 1
unaryNegative = -number
unaryPositive = +number

print(f"COMPLEMENT OPERATION")
print(f"The number is {number} and the binary format is {bin(number)}")
print(f"The 1's complement is {onesComplement} & the binary is {bin(onesComplement)}")
print(f"The 2's complement is {twosComplement} & the binary is {bin(twosComplement)}")
print(f"The unary negative is {unaryNegative} & the binary is {bin(unaryNegative)}")
print(f"The unary positive is {unaryPositive} & the binary is {bin(unaryPositive)}")
