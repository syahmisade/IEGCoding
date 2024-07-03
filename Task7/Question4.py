'''
For this exercise, you need to know two things about them:
Each resistor has a resistance value. Resistors are small - so small in fact that if you printed the resistance value on them, 
it would be hard to read. To get around this problem, manufacturers print color-coded bands onto the resistors to denote their resistance values. 
Each band has a position and a numeric value. The first 2 bands of a resistor have a simple encoding scheme: each color maps to a single number.
For example, if they printed a brown band (value 1) followed by a green band (value 5), it would translate to the number 15.
In this exercise you are going to create a helpful program so that you don't have to remember the values of the bands. 
The program will take color names as input and output a two digit number, even if the input is more than two colors!
The band colors are encoded as follows:
1.   Black: 0
2.   Brown: 1
3.   Red: 2
4.   Orange: 3
5.   Yellow: 4
6.   Green: 5
7.   Blue: 6
8.   Violet: 7
9.   Grey: 8
10.  White: 9
From the example above:
brown-green should return 15
brown-green-violet should return 15 too, ignoring the third color
'''

class Resistor:
    def __init__(self, color0, color1, colornone=""):
        self.color0 = color0
        self.color1 = color1
        self.colorN = colornone
    
    # def 
        
        