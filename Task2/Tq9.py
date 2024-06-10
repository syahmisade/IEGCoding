x = int(input("Enter a number: "))
numSq = 0

if(x>=0 and x<=3): #0,1,2,3
    numSq = x**2
    numRevSq = x**2
    revRevNumSq = numRevSq

    if(numSq == revRevNumSq):
        print(f"{x} is an Adam Number")
    else:
        print(f"{x} is not an Adam Number")
elif(x>3 and x<10):#4<9
    # print("1 digit")
    numSq = x**2
    numRevSq = x**2

    revRevNumSq = numRevSq % 10
    y = numRevSq // 10
    revRevNumSq = (revRevNumSq*10)+y
    # print(numSq)
    # print(revRevNumSq)
    if(numSq == revRevNumSq):
        print(f"{x} is an Adam Number")
    else:
        print(f"{x} is not an Adam Number")
elif(x>=10 and x<100):#10<99
    print("2 digit")
    numSq = x**2
    numRevSq = x**2

    revRevNumSq = numRevSq % 10
    y = numRevSq // 10
    revRevNumSq = (revRevNumSq*10)+y
    y = numRevSq // 10
    # print(numSq)
    # print(revRevNumSq)
elif(x>=100 and x<1000):
    print("3 digit")
elif(x>=1000 and x<10000):
    print("4 digit")
else:
    print("Error")