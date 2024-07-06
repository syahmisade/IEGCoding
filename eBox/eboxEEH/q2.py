'''
Write a Python program that accepts two numbers as input (say x and y) and finds x/y.
When the denominator is 0, the program should raise a ZeroDivisionError Exception and 
print the message shown in the sample output.
When there is an error in value in any of the 2 input arguments, the program should raise a 
ValueError Exception and print the message shown in the sample output.
Check for ValueError Exception while performing the division.
Input Format:
Input consists of 2 integers
Output Format:
Output is either the result or the error message.
Refer sample output.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
Enter number 1
6
Enter number 2
3
2.0
Sample Input and Output 2:
Enter number 1
5
Enter number 2
O
Divide By Zero Error
Sample Input and Output 3:
Enter number 1
t
Enter number 2
5
Invalid Value
'''


def divide_numbers():
    try:
        x = input("Enter number 1\n")
        y = input("Enter number 2\n")

        result = int(x) / int(y)
        print(result)

    except ValueError:
        print("Invalid Value")
    except ZeroDivisionError:
        print("Divide By Zero Error")


divide_numbers()
