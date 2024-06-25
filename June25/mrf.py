'''
Lectured by Mr.Jagen

Function: Map,Reduce,Filter
- Map:
    - Takes 2 parameter (function,the list)
    - For loop is inside this map
    - NEED to use list() function to display the map() => list(map(function,list))
    - What is in map() function:
        - def map(func):
            result = []
            for value in values:
                result.append(func(value))
            return result

- Reduce:
    - Not a build-in function
    - Need to import functools
    - Take 3 parameter: function(),sequence(),initial() but we use 2 for the time being
    - What is in reduce() function:
        - def reduce(func,list):
            result = list[0]
            for x in list:
                result = func(result,x)
            return result

- Filter:
    - Takes 2 parameter (function,the list)
    - Must return Boolean value
    - For loop is inside this filter
    - NEED to use list() function to display the filter() => list(filter(function,list))
'''
#--- Map ---------------------------------------------
print("Map "+"-"*50)

def kiraSst(harga):
    hargaSst = harga + (harga * 0.06)
    statement = f"{hargaSst:.2f}"
    return statement

hargaList = [12,23,34,45,56,67]

hargaSst = list(map(kiraSst,hargaList))

hargaSstStr = list(map(str,hargaList))

print(hargaSst)
print(hargaSstStr)

#--- Reduce ------------------------------------------
print("Reduce "+"-"*50)

# reduce(a,b,c)
from functools import reduce

num = [1,2,3]

def findTotal(old,current):
    return old + current

def factorial(old,current):
    return old * current

x = reduce(findTotal,num)
y = reduce(factorial,num,5)

print(x) 
print(y) # it will initialize the sum variables with 1 if use multiplication

#--- Filter ------------------------------------------
print("Filter "+"-"*50)

def findMultiOf3(n):
    return True if n % 3 == 0 else False

mO3 = filter(findMultiOf3,range(1,51))
print(list(mO3))