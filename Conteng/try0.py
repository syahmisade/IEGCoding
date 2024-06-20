
# Sample Input:
# 5
# Sample Output:
# /////\\\\\/////\\\\\
# /////\\\\\//////\\\\\
# /////\\\\\/////\\\\\
# /////\\\\\//////\\\\\
 
# Sample Input:
# 10
# Sample Output:
# //////////\\\\\\\\\\//////////\\\\\\\\\\
# //////////\\\\\\\\\\//////////\\\\\\\\\\
# //////////\\\\\\\\\\//////////\\\\\\\\\\
# //////////\\\\\\\\\\//////////\\\\\\\\\\

x = int(input())
kali = 2
level = 4

for i in range(level):
    for y in range(0,kali):
        for i in range(0,x):
            print("/",end="")
        for i in range(0,x):
            print("\\",end="")
    print()

