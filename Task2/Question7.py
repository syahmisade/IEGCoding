side1 = float(input("Enter a length for first side of triangle: "))
side2 = float(input("Enter a length for second side of triangle: "))
side3 = float(input("Enter a length for third side of triangle: "))

if(side1==side2 and side1==side3 and side2==side3):
    print("The triangle is an equilateral.")
elif(side1==side2 or side1==side3 or side2==side3):
    print("The triangle is an isosceles.")
else:
    print("The triangle is a scalene")

