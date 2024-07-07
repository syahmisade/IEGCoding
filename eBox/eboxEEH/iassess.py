'''
An input list is given in the code template.
Write a program to find the sum of first n values from the given list.
For invalid ‘n’ values, raise an IndexError Exception and 
display the message shown in the sample output.
Input and Output Format:
Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
[2, 3, 1, 5, 6, 7, 1]
Enter n
5
Sum = 17
Sample Input and Output 2:
[2, 3, 1, 5, 6, 7, 1]
Enter n
10
Index Value out of range
'''
# try:
#     numlist = [2, 3, 1, 5, 6, 7, 1]
#     print(numlist)

#     # fill your code
#     x = input("Enter n\n")
#     x = int(x)

#     sumNum = sum(numlist)

#     if x > len(numlist):
#         raise IndexError("Index Value out of range")

#     print(f"Sum = {sumNum}")
# except ValueError:
#     print("Invalid Input")

numlist = [2, 3, 1, 5, 6, 7, 1]
print(numlist)
n = int(input("Enter n\n"))
try:
    sum = 0
    for i in range(n):
        sum += numlist[i]
    print("Sum =", sum)

except IndexError:
    print("Index Value out of range")

# -----------------------------------------------------------------------------
'''

'''
username = input("Enter the username\n")
password = input("Enter the password\n")

class CustomError(Exception):
    pass

low_case = 0
up_case = 0
num_case = 0

for i in password:
    if i.islower():
        low_case += 1
    if i.isupper():
        up_case += 1
    if i.isdecimal():
        num_case += 1

try:
    if low_case >= 1 and up_case >= 1 and num_case >=1:
        print(f"Employee Username: {username}\nPassword: {password}")
    else:
        raise CustomError
except:
    print("CustomException: Invalid Password Exception")
