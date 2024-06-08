
a0 = int(input("PLEASE ENTER A 2 DIGIT NUMBER: "))

result = a0 % 10
a1 = a0 // 10

result = (result*10)+(a1%10)
# a2 = a1 // 10 

# print(a0,result) 

squreOri = a0**2
revSquare = result**2

# print(squreOri,revSquare)

####################################################################

b0 = revSquare

rrs = b0 % 10
b1 = b0 // 10

rrs = (rrs*10)+(b1%10)
b2 = b1 // 10 

rrs = (rrs*10)+(b2%10)
b3 = b2 // 10

# print(b0,rrs)

#####################################################################

if(squreOri == rrs):
    print(f"{a0} is an Adam Number")
else:
    print(f"{a0} is not an Adam Number")