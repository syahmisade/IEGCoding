'''
Prompts the user to enter their weight in kilograms and height in meters. Calculates the Body Mass Index (BMI). 
Prints the BMI. (Hint: The formula to calculate BMI is: BMI = weight / (height * height))
'''
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight/(height*height)

print(f"Your BMI is {bmi:.2f}")
