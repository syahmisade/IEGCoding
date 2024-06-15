import sys

cmdarguments = sys.argv
print(cmdarguments)

total = 0
for number in cmdarguments[1:]:  # loop from [1] until the end of the list
    total = total + int(number)
    # print(total) # Ni nnt print satu demi satu dalam cmd
print(total)
