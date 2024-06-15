# x = 3*1**3
# x=22%3
# x=4+3%5
# a = 16
# b = 15
# x=a% b //a
# x = int(43.55+2/2)
# x=2**(3**2)

# print(float (22//3 + 3/3))
# print(x, (2**3)**2,2**3**2)

# x=5
# y=10
# x = x ^ y
# y = x ^ y
# x = x ^ y
# print("X=%d, Y=%d"%(x,y))

# x=5
# k= x+6j
# print("Real part: %d\nImaginary part: %d" % (k.real,k.imag))

# x = "B"
# y = ord(x)
# print(y)

# x = 15
# y0 = oct(x)
# y1 = hex(x)
# print(y0,y1)

# a = 8+4j
# print(a, "is complex number?",isinstance(a,complex))

# x = 60/4
# print(x) #15.0

# x = (2750-800)//130
# print(x) #200

# rev = int(str(12)[::-1])
# print(rev)

# num = str(123)
# y = list(map(int, num))
# print(y)

n = 152
digitAmount = len(str(n))
digits = list(map(int, str(n)))
armstrongNum = []
total = 0

for digit in digits:
    cubeDigit = digit**digitAmount
    total += cubeDigit
print(total)

if n == total:
    print(f"{n} is a Armstrong Number")
else:
    print(f"{n} is not a Armstrong Number")

tm nb 
