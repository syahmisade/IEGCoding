x = 0b10101100
y = 0b11011001

# 1. lower 4 bits
mask = 0b00001111
lowerFB = x&mask
print("Lower 4 bits of x: ", bin(lowerFB))

# 2. Check y is odd or even
if (y & 1) :
    print("y is odd")
else:
    print("y is even")

# 3. Clear upper 4 bits
mask = 0b11110000
upperFB = x&mask
print("Clear upper 4 bits of x: ", bin(upperFB))

# 4. Check if the 5th bit of y is set
if (y & 0b00010000) :
    print("5th bit of y is set")
else:
    print("5th bit of y is not set")