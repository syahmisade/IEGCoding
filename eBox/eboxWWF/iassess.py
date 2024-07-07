# Prakash is the English school teacher at Aksh public school. He wants to teach the English characters to the 1st class students. 
# After taking the class he wanted to know whether his 
# students recognize the letters of English alphabet. 
# So he gave his students a English sentence, and asked them to write down the count of each character in alphabatical order.

# Help the students to find the count by writing a program that builds a frequency listing of the characters contained in the file, and 
# prints a sorted and formatted character frequency table to the screen.
 
# Note:
# Read the input from the file and print the output in the console.  
# Input File should be named as frequencyFile.txt.
 
# Input File Content:
# Set of words (or sentences).  
 
# Output Format:  
# Print a sorted and formatted character frequency table. 

# Sample Input and Output: 
# b: 1
# i: 1
# n: 2
# o: 2
# r: 1
# t: 1
# w: 1

# def readAlp(filename):
#     file = open(filename,"r")
#     rfile = file.read().lower()
    
#     dicT = {}
    
#     for letter in rfile:
#         if letter.isalpha():
#             if letter in dicT:
#                 dicT[letter] += 1
#             else:
#                 dicT[letter] = 1
    
#     sortLetter = dict(sorted(dicT.items()))
    
#     for i, j in sortLetter.items():
#         print(f"{i}: {j}")
    
# filename = "frequencyFile.txt"

# readAlp(filename)
#----------------------------------------------------------------------------------------------------------------------------------------------

# Saahil is working as a Receptionist at ABC Engineering College. The CSE department is conducting interview for the post of Asst. 
# Professor. He was asked to note down the salary expectation of all the interviewees. Due to some error with MS Excel software and 
# he is not able to write the details in the CSV format. So help him by writing a program that would write the given data to a file, and 
# finally print the file content.

# Note :
# Read the input from the console and write the output to a file.

# The name of the output file should be "salaryData.csv".

# Input Format:
# First Line is an integer corresponding to 'n' the number of persons.
# next n*2 lines corresponds to each persons name and salary.

# Sample Input:
# 4
# nisha
# 30000
# karthikeyan
# 40000
# krishna
# 30000
# shakthi
# 35000

# Output File Format:
# nisha,30000
# karthikeyan,40000
# krishna,30000
# shakthi,35000

def createFile():
    n = int(input("Enter the number of persons: "))
    
    count = 0
    salarydata = []
    
    while count<n:
        name = input()
        salary = int(input())
        salarydata.append(f"{name},{salary}")
        
        count+=1
    
    with open("salaryData.csv","w") as f:
        for i in salarydata:
            f.write(i+"\n")
    
    with open("salaryData.csv","r") as f:
        read = f.read()
        print(read)

createFile()