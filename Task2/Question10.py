x = int(input("PLEASE ENTER 3 DIGIT ONLY: "))

a0 = x % 10 # third digit

b0 = x // 10
b0 = b0 % 10 # second digit

c0 = x // 100 # first digit

result = c0**3 + b0**3 + a0**3

if(x == result):
    print(f"{x} is an Armstrong Number")
else:
    print(f"{x} is not an Armstrong Number")

#153,370,470,371