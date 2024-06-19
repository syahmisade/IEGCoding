'''
Lecture by Mr.Jagen

Functions -> for easier code maintainance issues
(organizing the code)
- Not for solving problems. Just build for organizing codes. Thats all.
- Functions are like a box where you can put your code in it and use it whenever you want
- You can use it multiple times in your program
- You can pass arguments to a function
- You can return values from a function
- You can also use default values for arguments
- Keyword for function:
    - Function name
    - Paranthesis -> ()
    - Parameter/s -> (if any)
    - Colon -> :
    - Indentation
- Call a function:
    - Function name
    - Paranthesis -> ()
    - Argument/s -> (if any)
- I can return a list -> return [a,b,c]
- I can return multiple values as tuples -> return a,b,c 
'''
def sayStatement(num): # Example of a function
    if num == 0:
        print("Hello, World")
    elif num == 1:
        print("Hello, World!")
    else:
        print("Hello, World!!!")

def greeting(name):
    print(f"Hello {name}, Nice to see you!")

def findTotal(x,y,z):
    total = x+y+z
    print(f"Result: {total}")

def buyLunch(foods,drinks):
    prices = []
    for food in foods:
        if food == "Nasi":
            prices.append(2.80)
        elif food == "Ayam":
            prices.append(3.50)
    for drink in drinks:
        if drink == "Limau Ais":
            prices.append(1.50)
    
    return prices
    # totalPrices = sum(prices)

    # print(f"I bought {foods} and {drinks} for lunch and the prices is RM{totalPrices:.2f}")

def simpleInterest(princple,period,rate):
    interest = (princple*period*rate)/100
    return interest

def participantList(name1,name2,name3):
    name1 = "DC " + name1
    name2 = "ML " + name2
    name3 = "GD " + name3
    return name1,name2,name3 # types: Tuple (Read Only List)
'''

# This are the function's exucations #####################################################

'''
# Calling def sayStatement
sayStatement(1) 

print("#"*50) #####################################################

# Calling def greetings
greeting("Syahmi") 

print("#"*50) #####################################################

# Calling def findTotal
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
findTotal(x,y,z) 

print("#"*50) #####################################################

# Calling def buyLunch (Total prices for the lunch)
itemPrices = buyLunch(["Nasi","Ayam"],["Limau Ais"]) 
total = 0
for prices in itemPrices:
    total += prices
print(f"The total prices for lunch: RM{total:.2f}")

print("#"*50) #####################################################

# Calling def simpleInterest
print(f"The amount of Interest: {simpleInterest(1000,1,6)}")

print("#"*50) #####################################################

# Calling def participantList
result = participantList("Hanafi","Syahmi","Samsol")
print(result)
print(type(result))