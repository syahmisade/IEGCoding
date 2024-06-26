'''
Input and Output Format:
Refer to sample input and output for formatting specifications.
print “Client not found” if search not found. else print the details as in the mentioned format below.

Note: All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output 1:
Enter the number of clients
2
Enter the details of the client 1
Shri
shri@mail.com
7346218
Enter the details of the client 2
Veena
veena@mail.com
8639124
Enter the passport number of the client to be searched
7346218
Client Details
Shri--shri@mail.com--7346218

Sample Input and Output 2:
Enter the number of clients
2
Enter the details of the client 1
Shri
shri@mail.com
7346218
Enter the details of the client 2
Veena
veena@mail.com
8639124
Enter the passport number of the client to be searched
2346718
Client not found
'''
x = int(input("Enter the number of clients\n"))
dictPass = {}

for i in range(x):
    name = input(f"Enter the details of the client {i + 1}\n")
    email = input()
    passport = input()
    dictPass[passport] = f"{name}--{email}--{passport}"

print(dictPass)

# y = input("Enter the passport number of the client to be searched\n")
# if y in dictPass:
#     print(f"Client Details\n{dictPass[y]}")
# else:
#     print("Client not found")

    