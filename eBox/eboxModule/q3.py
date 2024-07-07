'''
In a school, class teacher wants to organize a game for L.K.G students and the game is 
like there will be a  basket  with numbered balls teacher will give one number and 
student has to search for that particular  numbered ball if student found that  numbered ball  
then he has to say "Got It!" otherwise  "Sorry!".
Help the students to write a program to search the numbered ball.
Input  Format: 
The first line of input corresponds to the number of balls in the basket,n.
The next n  line of input consists of the numbered balls in the basket.
The last line of input consists of a numbered ball to be searched.
Output Format:
The output is a  string consist of 'Got It!' or 'Sorry!' (without quotes).
[All text in bold corresponds to input and the rest corresponds to output.]
Sample Input and Output 1:
5
21
18
90
6
74
6
Got It!
Sample Input and Output 2:
5
21
18
90
6
74
10
Sorry!
'''
n = int(input())
basket = []

for i in range(n):
    basket.append(int(input()))

ball = int(input())

if ball in basket:
    print("Got It!")
else:
    print("Sorry!")
