volSol = float(input("Enter solution required in litre: "))
mixSol = float(input("Enter the mixing solution in %: "))/100
solA = float(input("Enter first solution concentration in %: "))/100
solB = float(input("Enter second solution concentration in %: "))/100

volB = ((volSol*mixSol) - (solA*volSol))/(-solA+solB)
volA = volSol - volB

print(f"\nVolume of first solution required: {volA:.2f} litres")
print(f"Volume of second solution required: {volB:.2f} litres\n")

if(volA>3):
    print("First solution is not available, please order 1.3 liter now")
else:
    print("First solution is available can proceed")

if(volB>3):
    print("Second solution is not available, please order 1.3 liter now")
else:
    print("Second solution is available can proceed")