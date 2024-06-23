'''
Write a program to convert a Roman numeral to an integer and also convert integer to Roman numeral
'''
def romToNum(romNum):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romNumL = list(romNum)
    listNum = []
    result = 0

    for num in romNumL:
        print(roman_numerals.get(num, 0))
        listNum.append(roman_numerals.get(num, 0))
    for i in listNum:
        if listNum.index(i) > 0 and i > listNum[listNum.index(i) - 1]:
            result += i - 2 * listNum[listNum.index(i) - 1]
        else:
            result += i

    statement = print(result)
    return statement

romToNum("XIV")
#####################################################################

# int_val = int(input("Enter an integer: "))

# # Dictionary for Roman numeral values and symbols
# roman_numerals = {
#     1000: "M", 900: "CM", 500: "D", 400: "CD",
#     100: "C", 90: "XC", 50: "L", 40: "XL",
#     10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
# }

# roman_numeral = ''

# # Iterate over the dictionary items
# for value, symbol in roman_numerals.items():
#     while int_val >= value:
#         roman_numeral += symbol
#         int_val -= value

# print("The Roman numeral is ", roman_numeral)

