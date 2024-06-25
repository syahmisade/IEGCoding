# --- Function ------------------------------------------------------------------------------------------------

def minus(a,b):
    return a - b

def plus(a,b):
    return a + b

def multiplication(a,b):
    return a*b

def bahagi(a,b):
    return a/b

def kuasa(a,b):
    return a**b
#--- Function to collect the function (another way to do it but not efision) ----------------------------------

def arithmetic(keyword,a,b):
    if keyword == "sum":
        return plus(a,b)
    elif keyword == "minus":
        return minus(a,b)
    # elif keyword == "multiply":
    #     return multiplication(a,b)
    
#--- The best one to create a function inside function---------------------------------------------------------

def arith(x,a,b):
    return x(a,b)

#--------------------------------------------------------------------------------------------------------------

minus = arith(minus,10,90) # pass another function as an arguments to another function
plus = arith(plus,10,90)
multiply = arith(multiplication,12,3)
bahagi = arith(bahagi,12,2)
kuasa = arith(kuasa,12,2)
