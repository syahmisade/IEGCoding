'''
Explaination from Mr.Jegan
8 bit system, 
- Unsigned numbers (positive number)
    5 -> 0000 0101
- Signed numbers (positive and negative number)
    5 -> 0000 0101
    -5 -> 1111 1011 (1s complement) -6
        -> 1111 1011 (2s complement) -5
    * first bit zero == positive number
    * first bit one == negative number
        -> if negative, take the 2s complement => 

Example:
The given number is signed number
-6
6     0000 0110
1sC   1111 1001
2sC   1111 1010
'''
#1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
hexadecimalnumber = 0xF
#1,2,3,4,5,6,7,10,11,12,13,14,15
octalnumber = 0o10

print(hexadecimalnumber) # 15
print(hex(hexadecimalnumber)) # 0xF
print(octalnumber) # 8
print(oct(octalnumber)) # 0o10


