'''
Relationship student & alumni
'''

class Student:
    
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
        self.ic = ""
    
    def __str__(self):
        message = f"Firstname = {self.fn}\n"
        message += f"Lastname = {self.ln}\n"
        message += f"IC number = {self.ic}\n"
        return message

class Alumni(Student):
    
    def __init__(self, fn, ln, gy, dgree, an):
        super().__init__(fn,ln) # type: ignore
        self.gy = gy
        self.dgree = dgree
        self.an = an
    
    def __str__(self):
        message = f"Firstname = {self.fn}\n"
        message += f"Lastname = {self.ln}\n"
        message += f"IC number = {self.ic}\n"
        message += f"Graduation year = {self.gy}\n"
        message += f"Degree course = {self.dgree}\n"
        message += f"Alumni number = {self.an}\n"
        return message

#--- ROC (Range Of Classes) ----------------------------------------------------------------------------

alumni = Alumni("Abu","Harey",2022,"Software Engineering",1011101) # type: ignore
print(alumni)

