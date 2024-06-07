wd = int(input("Enter the amount of cash withdrawal: "))

if(wd%10>0):
    print("Invalid withdrawal amount. Please enter a multiple of 10.")
else:
    fifty = wd//50
    wd = wd%50
    twenty = wd//20
    wd = wd%20
    ten = wd//10
    print(f"{fifty} 50 dollar bill, {twenty} 20 dollar bill, {ten} 10 dollar bill")

    
