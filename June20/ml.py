'''
Lecture by Mr.Jegan
'''
def total(x):
    total = 0
    for i in x:
        total += i
    statement = print(f"The total for the numbers are {total}")
    return statement

def simpleInterest(princple=1000,period=1,rate=6): # We can create a default value (princple=1000,period=1,rate=6)
    interest = (princple*period*rate)/100
    statement = print(f"The interest is RM {interest:.2f}")
    return statement

def calTotal(*x):
    total = 0
    for i in x:
        total += i
    statement = print(f"The total for the numbers are {total}")
    return statement

def letterFruits(*fruits):
    fruitsList = []
    for i in fruits:
        if len(fruits) == 6:
            fruitsList.append(i)
    statement = print(f"The fruit with 6 digits are {fruitsList}")
    return statement

def exampleList(*x):
    for i in x:
        print(f"{i}",end=" ")

simpleInterest(rate=5) # We can use named arguments
simpleInterest(princple=5000,rate=7)
print("#"*50)
total([10,20,30])
total([10,20,30,40,50,60,70,80])
print("#"*50)
calTotal(10,20,30)
print("#"*50)
letterFruits("apple","banana","orange","grape","mango","dragonfruit")
print("#"*50)
exampleList("apple",2,"orange",3,"mango",70)