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
            print(f"Second Highest mark of {name}: {marks[-2]}")
else:
    print("Student doesn't exist")