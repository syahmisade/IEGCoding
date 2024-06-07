'''
Decision Making
'''
# find if the given number is positive, negative, zero
# find whether the business is making profit, loss or breakeven

sales = float(input("How much sales: "))
expenses = float(input("How much expenses: "))

amount = sales - expenses
profit = sales>expenses
losses = sales<expenses
breakeven = sales==expenses

if(profit):
    print(f"You are making {amount} profit my G")
    print("You can buy Benz with the bread now!")
elif(losses):
    print(f"You are making losses of {amount} my G")
    print("It's not looking good bruv. You need to work harder my G")
elif(breakeven):
    print("You are breakeven my G. All good G")

print(" ")
print("="*10)
print("TQVM")