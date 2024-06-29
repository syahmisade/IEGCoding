# print("Please choose:\n 1. Roman numeral to Integer.\n 2. Integer to Roman numeral")
# n = int(input())

# if n == 1:
#     roman_numeral = input("Enter a Roman numeral: ")

#     # make a dictonaries of data type
#     roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     int_val = 0

#     for i in range(len(roman_numeral)):
#         if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i - 1]]:
#             int_val += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i - 1]]
#         else:
#             int_val += roman_numerals[roman_numeral[i]]
#     print("The integer value is ", int_val)

# elif n == 2:
#     int_val = int(input("Enter an integer: "))

#     # make a list of data type
#     val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

#     roman_numeral = ''
#     i = 0

#     while int_val > 0:
#         for _ in range(int_val // val[i]):
#             roman_numeral += syb[i]
#             int_val -= val[i]
#         i += 1

#     print("The Roman numeral is ", roman_numeral)

# roman_numeral = input("Enter a Roman numeral: ")

# # Dictionary for Roman numeral values
# roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# int_val = 0

# for i in range(len(roman_numeral)):
#     current_value = roman_numerals.get(roman_numeral[i], 0)
#     if i > 0 and current_value > roman_numerals.get(roman_numeral[i - 1], 0):
#         int_val += current_value - 2 * roman_numerals.get(roman_numeral[i - 1], 0)
#     else:
#         int_val += current_value

# print("The integer value is ", int_val)

# roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# romNum = "XVI"
# romNumL = list(romNum)
# listNum = []
# result = 0

# for num in romNumL:
#     print(roman_numerals.get(num, 0))
#     listNum.append(roman_numerals.get(num, 0))
# for i in listNum:
#     if listNum.index(i) > 0 and i > listNum[listNum.index(i) - 1]:
#         result += i - 2 * listNum[listNum.index(i) - 1]
#     else:
#         result += i

# print(romNumL)
# print(listNum)
# print(result)

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

def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1
    previous_char = s[0]

    for char in s[1:]:
        if char == previous_char:
            count += 1
        else:
            compressed.append(previous_char + str(count))
            previous_char = char
            count = 1

    # Add the last set of characters
    compressed.append(previous_char + str(count))

    # Join the list into a final compressed string
    compressed_string = ''.join(compressed)

    # Return the original string if the compressed one is not smaller
    return compressed_string if len(compressed_string) < len(s) else s


# Example usage
input_string = "aabcccccaaa"
compressed_output = compress_string(input_string)
print(compressed_output)  # Output: a2b1c5a3
