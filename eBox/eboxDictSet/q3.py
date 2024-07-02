# You have a record of students. Each record contains the student's name and their percentage marks in Maths, Physics, and Chemistry. 
# The marks can be floating values. The user enters some integer followed by the names and marks of students. You are required to save the record in a 
# dictionary data type. The user then enters a student's name. The output is the average percentage marks obtained by that student, correct to two decimal places.

# Input and Output format:
# The first line contains the integer, which indicates the number of students, 'n'.
# The next 'n' lines contain the name and marks obtained by that student separated by a space. The final line contains the name of a 
# particular student previously listed to find the average mark of him.
# The output is the average of the marks obtained by the particular student correct to 2 decimal places.

# Note: Use Dictionary concept to solve the problem.
# Sample Input 1:
# 4
# aaa 35 67 89
# bbb 45 46 48
# ccc 78 78 78
# ddd 78 90 89
# ddd
# Sample Output 1:
# Average Mark of is : 85.67
 

# Sample Input 2:
# 3
# aaa 46 78 89
# bbb 34 68 90
# ccc 13 56 34
# ccc
# Sample Output 2:
# Average Mark of is : 34.33


def avgMark(num):
    
    infolist = []
    listOflist = []

    while num>0:
        nameMarks = input().split()
        infolist.append(nameMarks)
        
        num-=1
    
    for i in infolist:
        dicT = {
            "name":i[0],
            "marks":list(map(int,i[1:]))
        }
        listOflist.append(dicT) 
    
    name = input()
    
    for i in listOflist:
        if i["name"] == name:
            avg = sum(i["marks"])/len(i["marks"])
    
    statement = print(f"Average Mark of is : {avg:.2f}")
    
    return statement

num = int(input())
avgMark(num)