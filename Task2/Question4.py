number1 = int(input("Choose your first number: "))
number2 = int(input("Choose your second number: "))
number3 = int(input("Choose your third number: "))

if(number1>number2 and number1>number3):
    print(f"The largest number is: {number1}")
elif(number2>number1 and number2>number3):
    print(f"The largest number is: {number2}")
elif(number3>number1 and number3>number2):
    print(f"The largest number is: {number3}")