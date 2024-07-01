'''
Prakash having N number of sets. Prakash wants to find the second-largest number. So first he wanted to find the union of all sets and then he returns the second largest number of the union sets.
--------------------------------------------------------------------------------
Image result for second largest number
So can u please help to write a program to find the second largest number of union set.input and output format specifications are shown below.
--------------------------------------------------------------------------------
Input Format Specifications:
--------------------------------------------------------------------------------
The first line of input consists of several sets you required.
The second-line consists of entering the inputs to the sets.
Note that print the elements in sorted order.
--------------------------------------------------------------------------------
Output Format Specifications:
--------------------------------------------------------------------------------
The first line of output contains the Union of all sets.
The second line of output contains the Second largest Number of Union sets.
Sample Input 1:
3
1,1
2,1
4,5
Sample Output 1:
set([1, 2, 4, 5])
4
'''
def union(n):
    listNum = []
    while n>0:
        a=input().split(",")
        listNum.append(a)
        
        n-=1
    
    return print(listNum)

n = int(input())
union(n)