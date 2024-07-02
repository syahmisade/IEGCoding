'''
Revision sikit
'''

contoh = input("Enter anything ") # In a string format
contohlist = contoh.strip().split(",") # create a list of string from the string format
listcth = list(map(int,contohlist))
setlist = set(listcth)
print(setlist)