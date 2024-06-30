'''
Write the program to open an input file and read the number of lines in the input file.
------------------------------------------------------------------------------------------
Input format:
Input is a file. Filename: input.txt
------------------------------------------------------------------------------------------
Output format:
The output will be the integer which is the number of lines in the file. Display the output in the console.
--------------------------------------------------------------------------------------
Sample Input file (input.txt):
C was invented to write an operating system called UNIX.
C is a successor of B language which was introduced around 1970
The language was formalized in 1988 by the American National Standard Institue (ANSI).
By 1973 UNIX OS almost totally written in C.
Today C is the most widely used System Programming Language.
Most of the state of the art software have been implemented using C.
Easy to learn
Structured language
It produces efficient programs.
It can handle low-level activities.
It can be compiled on a variety of computers.
------------------------------------------------------------------------------------------
Sample Output 1:
The file has 11 lines
'''


def numLine(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print("The file has", len(lines), "lines")
    return len(lines)
