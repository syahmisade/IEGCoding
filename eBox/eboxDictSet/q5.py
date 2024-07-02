# Raj wants to generate some random numbers for creating a new PIN for his debit card, every month. So he developed Program such a way that, 
# he will enter list random numbers which are having duplicate elements and it will return a set of distinct elements from that, 
# he will generate a new PIN for his card.So the program will take list elements, which are having duplicate elements, and 
# create a set of distinct elements, and sum the k elements every time. and generate the new set, which will have summed values. 
# if the subset is not having k elements it will not sum the remaining values, it will directly add remaining elements to the new set.
# So let us try to write a program to get a set of elements from the given list of elements.

# Problem Constraints:
# Use set() to create a set of elements.
 
# Input and Output Format:
# 1st input is a number indicates a total number of elements in the list.
# 2nd input is a String contains a list of numbers.
# 3rd input is number indicates K (number of elements need to sum every time)
# The output contains a set of elements after summing. ( Refer to sample output format).
 
# Note: All text in bold corresponds to the input and the rest corresponds to output.
 
# Sample Input and Output 1:
# 9
# 1 3 2 4 5 1 6 31 15
# [1, 2, 3, 4, 5, 6, 15, 31]
# 3
# [6, 15, 31]

# Explanation :
# If list is [1,3,2,4,5,1,6,31,15], after performing set operation it will result = set([1, 2, 3, 4, 5, 6, 15, 31]), 
# now need find sum of 3 elements Like 1+2+3= 6, 4+5+6=15 add to sum to new set, since there are no further 3 elements, 
# add remaining 2 elements 31 and 15 to new set.
# So it will result in set in sorted order with elements as [ 6, 15, 31].

# Sample Input and Output 2:
# 5
# 5 2 7 0 8
# [0, 2, 5, 7, 8]
# 2
# [2, 8, 12]

# def countSet(s):
    
#     result = 0
#     listResult = []
    
#     listNum = s.split()
#     settOfNum = set(map(int,listNum))
#     sortLON = sorted(list(settOfNum))

#     print(sortLON)
    
#     k = int(input())
#     count = 0
    
#     for i in range(0,len(sortLON),k):
#         count+=k
#         for j in range(i,count):
#             result += sortLON[j]
#         listResult.append(result)
#         result = 0
            
#         listResult.append(result)
    
#     print(listResult)


# question = int(input())
# string = input()
# countSet(string)

def create_summed_set(n, numbers_str):
    numbers_list = list(map(int, numbers_str.split()))
    
    unique_numbers = sorted(set(numbers_list))

    summed_set = set()

    print(unique_numbers)

    k = int(input())
    
    for i in range(0, len(unique_numbers), k):
        subset = unique_numbers[i:i+k]
        if len(subset) == k:
            summed_set.add(sum(subset))
        else:
            summed_set.update(subset)
    
    print(sorted(summed_set))

num = int(input())
string = input()
create_summed_set(num,string)


