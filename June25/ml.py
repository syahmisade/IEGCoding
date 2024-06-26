# --- Function ------------------------------------------------------------------------------------------------
'''
Function in function:
- Function can be defined inside another function.
- The inner function has access to the variables of the outer function.
    - a function name will called function object throught a function name
'''

def minus(a,b): # function name
    return a - b # function object

def plus(a,b): # function name
    return a + b # function object

def multiplication(a,b): # function name
    return a*b # function object

def bahagi(a,b): # function name
    return a/b # function object

def kuasa(a,b): # function name
    return a**b # function object
#--- Function to collect the function (another way to do it but not efision) ----------------------------------

def arithmetic(keyword,a,b):
    if keyword == "sum":
        return plus(a,b)
    elif keyword == "minus":
        return minus(a,b)
    # elif keyword == "multiply":
    #     return multiplication(a,b)
    
#--- The best one to create a function inside function---------------------------------------------------------

def arith(x,a,b): # function name
    return x(a,b)

#--------------------------------------------------------------------------------------------------------------

minus = arith(minus,10,90) # pass another function as an arguments to another function
plus = arith(plus,10,90)
multiply = arith(multiplication,12,3)
bahagi = arith(bahagi,12,2)
kuasa = arith(kuasa,12,2)
