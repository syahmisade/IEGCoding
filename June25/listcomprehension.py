'''
Lectured by Mr.Jagen

List Comprehension:
- List combine with for loop (application idea)
- Want to create a list ONLY
    - Create a whole new list based from another list
- Cannot use this method to create a changing values from a initialize variables
    - for example sum of number (result += i) things like that 
'''
# Example for simple list comprehension 
squares = [x**2 for x in range(1, 11)]
# print(squares)

# Example for list comprehension with a condition
evens = [x for x in range(1, 11) if x % 2 == 0]
# print(evens)

# Example for nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
# print(flat_list)

# Example for finding square numbers for even and odd numbers
evenSqr = [x**2 for x in range(1,11) if x % 2 ==0]
oddSqr = [x**2 for x in range(1,11) if x % 2 != 0]
# print(evenSqr)
# print(oddSqr)



