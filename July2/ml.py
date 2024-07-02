'''
Polymorphism:
- Polymorphism is the ability to take multiple forms.
- In Python, polymorphism is achieved by using the same function name for different functions.
- 2 type of method:
    - Method overiding
    - Duck typing
'''
class races: # Parents class
    
    def __init__(self):
        pass
    
    def doCarryObj(self):
        pass
    
class Melayu(races): # class child
    
    def __init__(self):
        pass
    
    def doCarryObj(self):
        print("Ahmad si melayu")    
    
class Cina(races): # class child
    
    def __init__(self):
        pass
    
    def doCarryObj(self):
        print("Ahong si cina")

class India(races): # class child
    
    def __init__(self):
        pass
    
    def doCarryObj(self):
        print("Kumar si india")
#---------------------------------

def getRace(name): # a function
    if "typeM" in name:
        return Melayu()
    elif "typeC" in name:
        return Cina()
    else:
        return India()
#--------------------------------

orang = getRace("bangsa typeC")
orang.doCarryObj()
print(type(orang))