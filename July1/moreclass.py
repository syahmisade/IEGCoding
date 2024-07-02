'''
Relationship student & alumni
'''

class Student:
    
    def __init__(self, fn, ln,ic):
        self.fn = fn
        self.ln = ln
        self.ic = ic
    
    def __str__(self):
        message = f"Firstname = {self.fn}\n"
        message += f"Lastname = {self.ln}\n"
        message += f"IC number = {self.ic}\n"
        return message
    
    def perbuatan(self):
        return print(f"Tengah buat apa tu {self.fn} {self.ln}")

class Alumni(Student):
    
    def __init__(self, fn, ln, ic, gy, dgree, an):
        super().__init__(fn,ln,ic) # type: ignore
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

# alumni = Alumni("Abu","Harey",2022,"Software Engineering",1011101) # type: ignore
# print(alumni)

murid = Student("Ahmad","Syahmi",123213)
# print(murid.fn)
# murid.perbuatan()
# print(murid)
# print(type(Student))