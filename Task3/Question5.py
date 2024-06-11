iMoney = float(input("Total money to spend in investment: RM"))
invA = float(input("Enter annual interest rate bank A in %: "))/100
invB = float(input("Enter annual interest rate bank B in %: "))/100
earned = float(input("Total annual interest earned: RM"))

bankB = (earned - (iMoney*invA))/((-invA) + invB)
bankA = iMoney - bankB

print(f"\nAmount of investment made in bank A: RM{bankA:.2f}")
print(f"Amount of investment made in bank B: RM{bankB:.2f}")


