'''
Prompts the user to enter the principal amount, rate of interest, time in years, and number of times interest is compounded per year. 
Calculates the compound interest. Prints the compound interest.

(Hint: The formula to calculate compound interest is: A=P(1+R/100n)nt where A is the amount, P is the principal amount, 
R is the annual interest rate, t is the time the money is invested for, and n is the number of times interest is compounded per year)
'''
pAmount = float(input("Enter principal amount: "))
rateInterest = float(input("Enter rate of interest: "))
timeYears = float(input("Enter time of years: "))
timesInterest = float(input("Enter number of times interest is compounded per year: "))

x = 1+rateInterest
y = 100*timesInterest
z = timeYears*timesInterest

compoundYear = pAmount*(x/y)*z

print(f"The compound interest is {compoundYear}")