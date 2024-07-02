class calculator:
    def __init__(self, num0, num1=0):
        self.n0 = num0
        self.n1 = num1
        
    def square(self):
        return self.n0**2
    
    def cube(self):
        return self.n0**3
    
    def plus(self):
        return self.n0 + self.n1
    
    def minus(self):
        return self.n0 - self.n1


# def calcuFunction():
    