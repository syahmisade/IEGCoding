'''
File focus: display txt into cmd
'''

file = open("otherexample.txt")
# readline = file.readlines()
# print(readline)
# # print(int("100\n"))
# num = 0
# for i in readline:
#     num += int(i)

# print(f"sum = {num}")

# -------------------------------------

file1 = open("anotherexample.txt")
readline1 = file1.readlines()  # Ni read SAHAJA without printing the contents
print(readline1)  # Printing what have been read
s = "65 Biache beshe"
# If kita run .insert() method ni dua kali, so dua kali lah benda tu terjadi
# readline1.insert(3, f"{s}\n")  # To insert new content inside the txt

file1 = open("anotherexample.txt", "w")
file1.writelines(readline1)  # Ni write SAHAJA without printing the contents
