'''
Input Format:
Read a sentence from the user
Output Format:
Display the number of occurrences of words in the sentence. 
Refer sample output.
Sample Input 1:
the the function using dict dict
Sample Output 1:
{'the': 2, 'function': 1, 'using': 1, 'dict': 2}
'''

inputUser = input().split(" ")
listUser = []
prev = inputUser[0]
count = 1
for i in inputUser[1:]:
    if prev == i:
        count+=1
    else:
        listUser.append((prev, count))
        prev = i
        count = 1

listUser.append((prev, count))

dictUser = dict(listUser)

# print(inputUser)
# print(listUser)
print(dictUser)