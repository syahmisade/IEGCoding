'''
Working with files:
- Can only assign 1 method to 1 var per time
    - Cannot have multiple method (including the var) in the same time
'''

# Open a file
file = open("ReadFile/example.txt", "rt")

# Read the file
# I can change the arguments to whatever I want (based from amount of letter I want including space)
read = file.read(10)  # It will print the next 10 letter
print(read)

# This will make you read line by line
read = file.readline()
print(read)
read = file.readline()
print(read)

# This will read all the lines and compile them in a list (This including the \n too if there is a linecut)
readLines = file.readlines()
print(readLines)
