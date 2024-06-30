'''
Maths teacher Mr. Chulbul Pandey teaching the concept of average to his 3rd class students. Now he wants to take the test to check that students are clear about average concept. So he given some words on the black board and ask the students to find the average length of the words written on the board.
-----------------------------------------------------------------------------------------
Help the students find the average word length, by writing a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens). 
-----------------------------------------------------------------------------------------
Note :   
Read the input from the file and print the output in the console. 
Input File should be named as averageLength.txt. 
-----------------------------------------------------------------------------------------
Input File Fomat :  
Sentences or sequence of words.   
-----------------------------------------------------------------------------------------
Output Format:   
Print an integer value which corresponds to the average word length of a text in a file. 
-----------------------------------------------------------------------------------------
Sample Output:  
4
'''
def avglen(filename):
    fileread = open(filename)
    words = fileread.read().split()
    lenWords = len(words)
    sumWords = 0
    for word in words:
        sumWords += len(word)
    return int(sumWords/lenWords)


print(avglen("averageLength.txt"))

# fileread = open("averageLength.txt")
# words = fileread.read().split()
# lenWords = len(words)


# print(words)
# print(lenWords)
