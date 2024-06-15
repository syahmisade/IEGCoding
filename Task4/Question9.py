'''
Write a python program that takes few numbers as command line argument. 
Find the average of those numbers.
'''
import sys

cmdarg = sys.argv[1:]
total = 0

for x in cmdarg:
    total += int(x)

average = total/len(cmdarg)
print(f"The average number of the {cmdarg} are: {average:.2f}")
