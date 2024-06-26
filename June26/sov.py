'''
Scope of variables:
- Global variable => global var
- Local variable => local var
- Nonlocal variable => nonlocal var

'''
#--- Scope of variables --------------------------------------------------------
x = 10

def printX():
    print(f"function printX(): {x}")

printX()
print(x)

def modifyX():
    x = 20
    print(f"function modifyX(): {x}")

modifyX()
print(x)

def traditionalModify():
    x = 15
    return x

x = traditionalModify()
print(x)

def pythonModify(): # if there is no variables x, this f(x) will give error
    global x # will not created locally
    x = 25
    print(f"function pythonModify(): {x}")

pythonModify()
print(x)

buah = "durian"
def myFunction():
    print(buah)
    # buah = "oren" # Dont do it like this
    
myFunction()