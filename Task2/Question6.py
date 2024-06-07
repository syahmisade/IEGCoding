height = float(input("Enter you height in meter: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/(height**2)
print(f"Your BMI is {bmi:.2f}")

if(bmi>=30):
    print("Condition: Obesity")
elif(bmi>=25 and bmi>29.9):
    print("Condition: Overweight")
elif(bmi>=18.5 and bmi<24.9):
    print("Condition: Normal weight")
elif(bmi<18.5):
    print("Condition: Underweight")