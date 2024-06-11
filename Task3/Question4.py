a = 0b10101000 
b = 0b01010100

# 1. Lower 4 bits for a
mask = 0b00001111
lowerFB = a & mask
print("Lower 4 bits of a:", bin(lowerFB))

# 2. Combine a and b using OR
combination = a | b
print("Combination of a and b using OR:", bin(combination))

# 3. Create mask for 2nd and 6th bits for a
mask = 0b00100010
masked = a & mask
print("Masked a for 2nd and 6th bits:", bin(masked))
