'''
Bitwise Operation (This only apply for binary)
'''

ownerpermission = 0b111 # 0b == represent binary number from basic decimal number
oPBit = "{0:b}".format(ownerpermission)

print(f"{ownerpermission} is the owner permission")
print(f"{oPBit} is the owner permission in binary format")

print("="*50)

filepermission = 0b111101001
fPBit = "{0:b}".format(filepermission)

print(f"{filepermission} is the file permission")
print(f"{fPBit} is the file permission in binary format")
#owner == Read,Write,Execute
#group == Read,Execute
#other == Execute

print("="*50)

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

print("="*50)

#AND Binary
andBit = (filepermission & mask) >> 3 # >> == movekan nombor sekian2 ke kanan #decimal
andBitBinary = "{0:b}".format(andBit)

print("AND OPERATION")
print(f"The binary for AND operation is {andBitBinary}") 
print(f"The decimal for AND operation is {andBit}") #decimal

print("="*50)

#OR Operation
orBit = filepermission | mask
orBitBinary = "{0:b}".format(orBit)

print("OR OPERATION")
print(f"The binary for OR operation is {orBitBinary}") 
print(f"The decimal for OR operation is {orBit}") #decimal

print("="*50)

'''
We can create a key based on ASCII character
This is more related on encrypted data or information
'''
# XOR Operation
message = 0b10100101
key = 0b11001100
encrypted_message = message ^ key
decrypted_message = encrypted_message ^ key

print("XOR OPERATION") 
print(f"The message is {message} and thebinary format is {bin(message)}")
print(f"The key is {key} and the binary format is {bin(key)}")
print(f"The encrypted message is {encrypted_message} in decimal and {bin(encrypted_message)} in binary")
print(f"The decrypted message is {decrypted_message} in decimal and {bin(decrypted_message)} in binary")