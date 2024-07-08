'''
Suresh playing a numbers game. The game description is  Suresh picks random numbers and 
calculate the sum of all numbers, and the problem is some times the sum of the 
numbers will be float value and he wants to modify that sum by using 
Floor(), Ceil(), Round() functions and finally, he wants to calculate the difference of 
these 3 functions.
Input Format specifications:
Input consists of a list of values separated by space.
Output Format Specifications:
The first line of output should be the difference between floor()sum - ceil()sum.
Secondly of output should be the difference between the ceil()sum - round()sum.
The third line of output should be the difference between floor()sum - round()sum.
Constraints:
Use only floor() and ceil() round() function Python
Sample Input 1:
23.34 12 25
Sample Output 1:
-1.0
1.0
0.0
Sample Input 2:
-21.23 -18.23 -12
Sample Output 2:
-1.0
0.0
-1.0
'''
import math


def main():

    num_list = list(map(float, input().split()))

    floor_sum = math.floor(sum(num_list))
    ceil_sum = math.ceil(sum(num_list))
    round_sum = round(sum(num_list))

    difFC = floor_sum - ceil_sum
    difCR = ceil_sum - round_sum
    difFR = floor_sum - round_sum

    print(f"{difFC:.1f}")
    print(f"{difCR:.1f}")
    print(f"{difFR:.1f}")


if __name__ == "__main__":
    main()
