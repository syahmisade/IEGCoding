'''
Prompts the user to enter the principal amount, rate of interest, and time in years. Calculates the simple interest. 
Prints the simple interest. (Hint: The formula to calculate simple interest is: SI = (P * R * T) / 100)
'''
pAmount = float(input("Enter principal amount: "))
rateInterest = float(input("Enter rate of interest: "))
timeYears = float(input("Enter time of years: "))

simpleInterest = (pAmount*rateInterest*timeYears)/100

print(f"The result for the simple interest: {simpleInterest}")