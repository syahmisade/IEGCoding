'''
Jack was a little boy, who was playing the game word puzzle. The jack brother gave him a task to 
find the nouns in a given set of lines. Try to help jack to finish his task.
Problem Constraints:
Use the re  module for Regular Expression
Use the findAll method
Extract all names from the given text. Use metacharacter
Rules:
1) only alphabets
2) starts with upper-case
3) may contain surnames
4) may contain initials
Input format:
A single line input string consists of capitalized words in it.
Output format:
The output will be the words which are obeying the mentioned rules
Sample Input 1:
S.Vinoth Kumar and John Watson are friends with James
Sample output 1:
S.Vinoth Kumar 
John Watson 
James
Sample Input 2:
there were two friends named Sam and Jason
Sample output 2:
Sam
Jason
'''
import re


def findNames(text):
    checks = re.findall(
        r'[A-Z](?:\.[A-Z])?[a-zA-Z]*(?: [A-Z](?:\.[A-Z])?[a-zA-Z]+)*', text)
    for check in checks:
        print(check)


# text = input()
# findNames(text)

# ------------------------------------------------------------------------------
'''
Ishan playing aa simple game with alphabets. the procedure will be Ishan choose aa random number in between (0-26) and 
then he changed the alphabets in Ceaser chipper(Each letter 'shifted'  wrt chosen number).
Image result for Caesar Cipher
So can you please help Ishan to write aa program for Ceaser cipher Encryption. Input and Output format Specifications are 
shown below.
Input Format Specifications:
The first line of Input contains a String.
The next line of input contains Integer N, N is the shifted positions number.
Replace all characters with the nth character from the current character.
 Must use "re.sub()".
Note: [" ord() expected a character, but a string of length 2 found" if the error shows like this then you use the 
lambda function ].
Output Format Specifications:
Output Consists of String.
if character addition is going greater than 127 then print ‘invalid’.
Sample Input and Output showed below.
Sample Input 1:
amphisoft
3
Sample Output 1:
dpsklvriw
Sample Input 2:
krishnamohan
27
Sample Output 2:
invalid
'''


def caesar_cipher_encrypt(text, shift):

    def shift_char(match):
        char = match.group(0)
        new_char = chr(ord(char) + shift)
        if ord(new_char) > 127:
            return "invalid"
        return new_char

    if shift > 26:
        return "invalid"

    pattern = re.compile(r'[a-zA-Z]')
    encrypted_text = re.sub(pattern, shift_char, text)

    if "invalid" in encrypted_text:
        return "invalid"
    return encrypted_text


input_string = input().strip()
shift_value = int(input().strip())

result = caesar_cipher_encrypt(input_string, shift_value)

# print(result)
