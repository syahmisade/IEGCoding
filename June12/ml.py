'''
Lecture by Mr.Jegan

*Pass value to another program -> program.py <<infromation OR argument<< using commandline 

Dictionary:
1. Keywords
2. Built-in function
3. Modules
    - Not built-in
    - Full of function
    - Must import them into our programme
    - Parse command line arguments -> sys 
        - sys module has a variable -> argv (type of list)
            - argv == variables OR function
            - Access variable inside the module -> dot operator "."
                Example:
                import sys
                print(sys.argv)
'''

# give us list to pass to the python
# Item position 0 were program name itself
# Command line arguments -> the program in the command line (string type)

import sys

cmdarguments = sys.argv
print(cmdarguments)

total = 0
for number in cmdarguments[1:]: # loop from [1] until the end of the list
    total = total + int(number)
    # print(total) # Ni nnt print satu demi satu dalam cmd
print(total)

print("="*50)
# ================================================================================

numbers = input("Enter the numbers to do Total: ")
numberList = numbers.split(",") # .split() == will split the space // .split(",") == split the coma (,)
print(numberList)

totalNum = 0
for num in numberList: 
    totalNum = totalNum + int(num)
print(totalNum)