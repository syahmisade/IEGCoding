'''
Akash wants to send a message to his colleague about his official team work. But he wants to maintain his message privacy, 
so he will encrypt his message and send that to his friend. Now his colleague wants to decode that message. 
Akash gave a hint to his colleague, like he has to decode his message by splitting his
message with a particular character sent by him. 
Help Akash's colleague to decode the message by writing a program.
Input Format:
The first line of input consists of a string.
The next line of input consists of a character.
Output Format:
The output is a list of strings after splitting.
Every first letter of splitted word should be in capital.
Note: All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
aaahggghbbb
h
Strings after splitting
Aaa
Ggg
Bbb
Sample Input and Output 2:
ahhg&hcg&fhgf90
&
Strings after splitting
Ahhg
Hcg
Fhgf90
'''
# Write your code here
# s = input()
# c = input()
# l = s.split(c)
# print("Strings after splitting")
# # for i in l:
# #     print(i[0].upper()+i[1:])
# for i in range(len(l)):
#     l[i] = l[i].capitalize()
#     print(l[i])

# -----------------------------------------------------------------------
'''
In Maple Casino, there is a play in which contestant hit a ball to two numbered plates, 
and then contestant has to say a number which is summation of all the prime numbers from 1 to 'n' , 
here 'n' represent the first plate number. And the operation will continue upto 't' times, 
here 't' represent the second plate number.
Explanation:
First we perform the sum operation of all the prime numbers from 1 to 7 i.e. {2,3,5,7}, 
the sum of these prime numbers is: 17.
Then, again we have to perform the sum of all the prime numbers from 1 to 17, which is the previous sum of prime numbers.
1 to 17: {2,3,5,7,11,13,17}, and the resultant sum of prime numbers is: 58.
This operation will continue upto 2 times (for above mentioned sample input).
Write a program to find the continous sum of prime numbers 't' times.
Input Format:
First line as integer which corresponds to last integer of prime series.
Second line as integer which corresponds to number of times we have to perform the sum operation of that prime series.
Output Format:
A line as integer which corresponds to sum of all the prime numbers.
Input Format:
7
2
Output Format:
Sum:58
'''


def primeNum(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


rangeNum = int(input())
times = int(input())
count = 0
while count < times:
    sumNum = 0
    for i in range(1, rangeNum+1):
        if primeNum(i):
            sumNum += i

    rangeNum = sumNum

    count += 1

print(f"Sum: {sumNum}")
