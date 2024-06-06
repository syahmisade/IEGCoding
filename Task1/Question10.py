'''
Converts the given binary 1011 to its decimal representation. Prints the decimal representation.
'''
binary = 1011

binary1 = 1011%10
binary2 = (1011//10)%10
binary3 = (1011//100)%10
binary4 = (1011//1000)%10

var1 = binary1*(2**0)
var2 = binary2*(2**1)
var3 = binary3*(2**2)
var4 = binary4*(2**3)

decimal = var1+var2+var3+var4

print(binary4,binary3,binary2,binary1)
print(f"The decimal representation of the binary number 1011 is {decimal}")