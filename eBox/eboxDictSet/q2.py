# Ramya wants to know about the dictionary data type. Now she wants to create a dictionary using a string like each unique character in 
# a string is considered as keys of dictionary and number of occurrence of each character considered as values of each key in a dictionary.

# Now she has to display the dictionary format and occurrence of characters in ascending order.

# Input and Output Format:
# Input is a string.
# The output contains dictionary representation in ascending order of characters and occurrence of each character in a string
# (Refer sample output format).

# All text in bold corresponds to the input and the rest corresponds to output [Refer sample input and output format].

# Sample Input 1:
# sandhyaa
# Sample Output 1:
# Dictionary of string: {'a': 3, 'd': 1, 'h': 1, 'n': 1, 's': 1, 'y': 1}
# a-- 3
# d-- 1
# h-- 1
# n-- 1
# s-- 1
# y-- 1

# Sample Input 2:
# aaaattttgggjjjiiibb
# Sample Output 2:
# Dictionary of string: {'a': 4, 'b': 2, 'g': 3, 'i': 3, 'j': 3, 't': 4}
# a-- 4
# b-- 2
# g-- 3
# i-- 3
# j-- 3
# t-- 4

# Sample Input 3:
# rathhaann
# Sample Output 3:

# Dictionary of string: {'a': 3, 'h': 2, 'r': 1, 't': 1, 'n': 2}
# a-- 3
# h-- 2
# n-- 2
# r-- 1
# t-- 1

def display(word):
    d = {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    sortedD = dict(sorted(d.items()))
    
    print(f"Dictionary of string: {sortedD}")
    for i in sorted(d):
        print(f"{i}-- {d[i]}")

word = input()
display(word)