#--- First Method ---------------------------------------------------
'''
import myModules

x = emyModules.calculate_simple_interst(1000,6,1)
print(x)

'''
#--- Second Method (Python Recommended)--------------------------------------------------
# The drawback: need to import each functions that you want
'''
from myModules import calculate_simple_interest

x = calculate_simple_interest(1000,6,1)
print(x)

'''
#--- Third Method -----------------------------------------------------------
from myModules import *

x = calculate_simple_interest(1000,6,1)
print(x)

y = add(12,34)
print(y)