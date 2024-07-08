'''
In the digital world, it's easy to access contact details of individuals through online. 
Users give permission to third party apps to access basic details making it easy for spammers to 
get more contacts. Hackers are using this contact numbers for making Spam calls 
(irrelevant or inappropriate call sent over the phone) to annoy the users. 
So to handle this issue Cyber Crime Department need to analyze the valid and 
spam call mobile number pattern. The valid phone number pattern should contain following things:
1. It should start with "+91-" 
2. Followed by ten digits
If any mobile number violating the above rules can be blocked immediatley.
Input and Output Format:
Input is a string .
Output is a string . Refer sample input and output for formatting specifications.
Sample input 1:
+91-9876543210
Sample output 1:
Not a Spam Call
Sample input 2:
9876543210
Sample output 2:
Spam Call
'''
import re


def is_valid_phone_number(phone_number):
    if re.match(r'^\+91-\d{10}$', phone_number):
        return "Not a Spam Call"
    else:
        return "Spam Call"


numphone = input()
print(is_valid_phone_number(numphone))
