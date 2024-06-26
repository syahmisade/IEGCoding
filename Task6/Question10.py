'''
Write a simple python function that accepts a hyphen-separated sequence of words as parameter and 
returns the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''

def hps(x):
    listHps = sorted(x.split("-"))
    joinHps = "-".join(listHps)
    
    return joinHps

x = input("Enter items with (-): ")
print(f"The answer: {hps(x)}")