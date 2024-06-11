x = 0b10101100 
y = 0b11010010

# 1. Swap value x and y w.o using temporary variable
print(f"value x before: {x}")
print(f"value y before: {y}")

x = x + y
y = x - y
x = x - y

print(f"value x after: {x}")
print(f"value y after: {y}")

# 2. Toggle the 3rd and 5th bits in x
x = 0b10101100
k = 0b00010100

toggle = x ^ k
print(f"Toggle 3rd and 5th bits for {bin(x)} is {bin(toggle)}")

# 3. Check if given 2 numbers are different
a = 29
b = 15

print(bin(a),bin(b))