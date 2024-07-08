'''
Swiggy is an online food ordering and delivery platform. 
For Holi festival they planned to give special offer upto 50% based on offer code shared by 
the Swiggy team. Due to lot of offer code forgery they set a pattern to create an offer code. 
The pattern for offer code was , it should be a word which contains all vowels. 
If there is any word without all vowels then that offer code was rejected by the swiggy team.
Input and Output Format:
Input is a string .Only lower case allowed.
Output is a string . Print “Accepted “ if offer code is valid else “Not Accepted” without quotes.
Refer sample input and output for formatting specifications.
Sample Input 1:
tragedious
Sample Output 1:
Accepted
Sample Input 2:
hello everyone
Sample Output 2:
Not Accepted
'''
import re


def check_offer_code(s):
    vowels = 'aeiou'
    for vowel in vowels:
        if not re.search(vowel, s):
            return "Not Accepted"
    return "Accepted"


string = input()
print(check_offer_code(string))
