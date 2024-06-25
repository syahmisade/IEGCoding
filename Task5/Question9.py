'''
Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
'''
def romToNum(romNum):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romNumL = list(romNum)
    result = 0
    prevNum = 0
    
    for i in romNumL[::-1]:
        if roman_numerals[i]>=prevNum:
           result +=  roman_numerals[i]
           prevNum = result
        else:
            result -= roman_numerals[i]
        

    statement = print(f"The Integer numeral is {result}")
    return statement


def numToRom(num):
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    roman_numeral = ''

    # Iterate over the dictionary items
    for value, symbol in roman_numerals.items():
        while num >= value:
            roman_numeral += symbol
            num -= value

    statement = print(f"The Roman numeral is {roman_numeral}")
    return statement


print("Choose\n 1. Roman number to integer\n 2. Integer to Roman number")
x = int(input(" "))
if x == 1:
    romNum = input("Enter the Roman numeral: ")
    romToNum(romNum)
elif x == 2:
    num = int(input("Enter the integer: "))
    numToRom(num)
else:
    print("Invalid choice")
