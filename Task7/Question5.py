'''
Your task is to Validate Credit Card Number
Given a number determine whether or not it is valid per the Luhn formula.
The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, 
such as credit card numbers and Canadian Social Insurance Numbers.
The task is to check if a given string is valid
Valid credit card number
4539 3195 0343 6467
The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling
4_3_ 3_9_ 0_4_ 6_6_
If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:
8569 6195 0383 3437
Then sum all of the digits:
8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80
If the sum is evenly divisible by 10, then the number is valid. This number is valid!
'''
def validation(n):
    listOfNum = list(n)
    
    intList = list(map(int,listOfNum))
    
    for i in range(len(intList)):
        if i%2 != 0:
            intList[i] = intList[i]*2
            if intList[i] > 9:
                intList[i] = intList[i] - 9
    
    sumNum = sum(intList)
    
    if sumNum%10 == 0:
        statement = "This number is valid"
    else:
        statement = "This number is not valid"

    return print(statement)

number = input("Enter credit card number to validate it: ").replace(" ","")
validation(number)

# def validation(n):
#     # Convert the input string to a list of integers
#     intList = list(map(int, n))
    
#     # Reverse the list to handle the Luhn algorithm from right to left
#     intList.reverse()

#     # Apply Luhn algorithm logic
#     for i in range(len(intList)):
#         if i % 2 != 0:
#             intList[i] = intList[i] * 2
#             if intList[i] > 9:
#                 intList[i] = intList[i] - 9
    
#     # Calculate the sum of the processed list
#     sumNum = sum(intList)
    
#     # Check if the sum is divisible by 10
#     if sumNum % 10 == 0:
#         statement = "This number is valid"
#     else:
#         statement = "This number is not valid"

#     return statement

# # Read input and remove any spaces
# number = input("Enter credit card number to validate it: ").replace(" ", "")
# print(validation(number))
