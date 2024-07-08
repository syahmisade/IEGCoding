'''
Tax Information Network (TIN) is an initiative by Income Tax Department of India (ITD) for 
the modernization of the current system for collection, processing, monitoring and accounting of 
direct taxes using information technology. The network will check the eligible entities based on 
Permanent Account Numbers (PAN).PAN contains ten-digits in which first five characters are letters, 
next four numerals, last character is a letter and all characters in PAN number is 
always uppercase.If the PAN given by the user follow the above format then it is a 
Valid PAN Number other wise Invalid PAN Number.
write a program to validate the PAN number.
Input and Output Format:
Input is string of any length of any case.
Output is string ,should print “Valid PAN Number” without quotes if input fits the 
PAN rules otherwise “Invalid PAN Number” without quotes.
Refer sample input and output for formatting specifications.
Sample Input 1:
ABCDE1234F
Sample Output 1:
Valid PAN Number
Sample Input 2:
12345ABCD3
Sample Output 2:
Invalid PAN Number
'''
import re


def validate_pan(pan):
    # pan = pan.upper()

    pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')

    if pattern.match(pan):
        return "Valid PAN Number"
    else:
        return "Invalid PAN Number"


pan = input().strip()
print(validate_pan(pan))

# def validate_pan_number(pan_number):
#     # Check length of PAN number
#     if len(pan_number) != 10:
#         return "Invalid PAN Number"

#     # Check first 5 characters are letters
#     if not pan_number[:5].isalpha():
#         return "Invalid PAN Number"

#     # Check next 4 characters are numbers
#     if not pan_number[5:9].isdigit():
#         return "Invalid PAN Number"

#     # Check last character is a letter
#     if not pan_number[9].isalpha():
#         return "Invalid PAN Number"

#     # Check all characters in PAN number are uppercase
#     if not pan_number.isupper():
#         return "Invalid PAN Number"

#     return "Valid PAN Number"

# def main():
#     pan_number = input()
#     print(validate_pan_number(pan_number))

# if __name__ == "__main__":
#     main()
