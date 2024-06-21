# Input format:
# The first line contains the integer, which indicates the number of students, 'n'.
# The next 'n' lines contain the name and marks obtained by that student separated by a space.
# The final line contains the name of a particular student to find the second-highest mark of him.

# Output format:
# The output is the second-highest mark obtained by the particular student. If he scored the same marks in all subjects, then print a message as shown sample I/O.
# If the student name does not exist then print  "Student doesn't exist". [Refer Sample I/O]

# Sample Input 1:
# 4
# Sandy 78 67 89 100
# John 45 46 48 23
# Cherry 78 78 78 78
# Ratan 78 90 89 56
# Sandy
# Sample Output 1:
# Second Highest mark of Sandy: 89
 

# Sample Input 2:
# 2
# sath 100 100 100 100
# jan 67 56 34 89
# sath
# Sample Output 2:
# sath scored same marks in all subjects: 100
# Sample Input 3:
# 2
# Ratan 78 90 89 56
# Sandy 78 67 89 100
# pooja
# Sample Output 3:
# Student doesn't exist

### Code 1 ###
n = int(input())
inputList = []
outputList = []

while len(inputList)<n:
    inputList.append(input().split(" "))

name = input()

for i in inputList:
    oList = {
        "name": i[0],
        "marks": list(map(int, i[1:]))
    }
    outputList.append(oList)

oDict = None

for j in outputList:
    if j["name"] == name:
        oDict = j
        break
    if j["name"] != name:
        oDict = False
        print("Student doesn't exist")
        break

if oDict:
     mark = sorted(oDict["marks"])
     for i in range(len(mark)-1):
        if mark[i] == mark[i+1]:
            print(f"{name} scored same marks in all subjects: {mark[i]}")
            break
        if mark[-1]>mark[-2]:
            print(f"Second Highest mark of {name}: {mark[-2]}")
            break


### Code 2 ############################################################################
n = int(input())
inputList = []
outputList = []

# Collect input for students
while len(inputList) < n:
    inputList.append(input().split())

name = input()

# Convert input to list of dictionaries
for i in inputList:
    oList = {
        "name": i[0],
        "marks": list(map(int, i[1:]))
    }
    outputList.append(oList)

oDict = None

# Search for the student by name
for j in outputList:
    if j["name"] == name:
        oDict = j
        break

if oDict:
    # If student is found, process the marks
    marks = sorted(oDict["marks"])
    if len(marks) > 1:
        # Check for any duplicate marks
        duplicate_found = False
        for i in range(len(marks) - 1):
            if marks[i] == marks[i + 1]:
                print(f"{name} scored same marks in all subjects: {marks[i]}")
                duplicate_found = True
                break

        # If no duplicates found, print the second-highest mark
        if not duplicate_found:
            print(f"Second highest mark of {name}: {marks[-2]}")
else:
    print("Student doesn't exist.")
