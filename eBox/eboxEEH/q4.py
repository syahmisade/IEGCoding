'''
Write a program that prompts users to enter numbers till he enters one positive number. 
Whenever the user enters a negative number or a string , raise a ValueError exception and 
handle it appropriately and display the message shown in the sample output.
Input and Output Format:
Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
Enter a positive integer
5
Good! You entered 5
Sample Input and Output 2:
Enter a positive integer
-6
You entered a negative number. Retry!
Enter a positive integer
-9
You entered a negative number. Retry!
Enter a positive integer
3
Good! You entered 3
'''
while True:
    try:
        x = input("Enter a positive integer\n")
        x = int(x)
        if x > 0:
            print(f"Good! You entered {x}")
            break
        else:
            raise ValueError("You entered a negative number. Retry!")
    except ValueError as e:
        print(e)


# while True:
#     try:
#         num = input("Enter a positive integer\n")
#         num = int(num)
#         if num <= 0:
#             raise ValueError("You entered a negative number. Retry!")
#         else:
#             print(f"Good! You entered {num}")
#             break
#     except ValueError as e:
#         print(e)
#         print("")
