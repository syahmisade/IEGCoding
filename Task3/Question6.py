x = 0b10101100
y = 0b11010010

# 1. Swap value x and y w.o using temporary variable
print(f"value x before: {x}")
print(f"value y before: {y}")

x = x ^ y
y = x ^ y
x = x ^ y

print(f"value x after: {x}")
print(f"value y after: {y}")

# 2. Toggle the 3rd and 5th bits in x
x = 0b10101100
k = 0b00010100

toggle = x ^ k
print(f"Toggle 3rd and 5th bits for {bin(x)} is {bin(toggle)}")

# 3. Check if given 2 numbers are different (tak tahu nak terang mcm mana)
a = 29
b = 15

binNum = a ^ b

if (binNum):
    print(f"{bin(a)} and {bin(b)} are 2 different numbers")
else:
    print(f"{bin(a)} and {bin(b)} are 2 same numbers")
