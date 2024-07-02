'''
If the relationship have a relationship -> become a properties
'''

class Cust:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
        self.ic = ""
        self.passp = ""
    
    def __str__(self):
        message = f"Firstname: {self.fn}\n"
        message = message + f"Lastname: {self.ln}\n"
        message = message + f"IC number: {self.ic}\n"
        message = message + f"Passport: {self.passp}\n"
        return message
    
    def setlastname(self,ln):
        self.ln = ln

class Passp:
    def __init__(self, negara, pnum):
        self.negara = negara
        self.pnum = pnum

    def __str__(self):
        string = f"{self.negara}: {self.pnum}"
        return string

#--- ROC (Range Of Classes) ----------------------------------------------------------------------------

# Create instances
man = Cust("Peter", "Parker")
passport = Passp("UK", "E023405RT")

# Assign passport to customer
man.passp = passport # type: ignore
dictMan = man.__dict__

print(man)
man.setlastname("Abu")
print(man)
# print(man.ln)

# Display customer and their passport information
# print(man)  # Output: Peter Parker
# print(man.passp)  # Output: UK: E023405RT
# print(man.__dict__)

