'''
Class:

- Possible to become different role based on the event
- Assign variables => creating a Class attributes
- def __init__() => a function : can be used into coding
    - self => a variable : can be used into coding (used as parameter in __init__())
- Another ways to collect data and display data gain from the input
- Try check balik nota sir
'''
class Ultraman:
    planet = "Nebula M60" # one of the Class attributes
    
    # this is an initializer (Instance Initialization) / Instance Attributes
    def __init__(self,name,power,warna): # Taking parameter
        self.planet = "Nebula M80" # one of the Instace Attributes (Example of without taking a parameter)
        self.name = name
        self.power = power
        self.__warna = warna
        self.host = {} # Initialize it as a blank so that we can submit something
        self.kaiju = [] # Initialize it as a blank so that we can submit something
    
    # This is a method => which have the same structure as functions
    def getKuasa(self):
        statement = f"Kuasa {self.name} : {self.power}"
        return statement

    def getWarna(self):
        statement = f"Warna {self.name} : {self.__warna}"
        return statement
    
    def setWarna(self,warna):
        self.__warna = warna
    
    def __str__(self):
        statement = f"{self.name} is from {self.planet}"
        return statement
    
    def hostInfo(self):
        print("Info about host:")
        print(self.host["Name"])
        print(self.host["Age"])
        print(self.host["Gender"])
    
    def kaijuInfo(self):
        print(f"Info about kaiju:")
        for program in self.kaiju:
            count = 1
            print(f"Kaiju No.{count}: {program}")
            count+=1
        

# --- Outside Class -----------------------------------------------------------------------------------------------------
    
# Calling Class including the instances:  how many Arguments (== "Ultraman Gaia",1000) will be depending on the Class's Initializer
ultraman = Ultraman("Gaia",500,"Merah Putih Emas Hitam")
name = f"Ultraman {ultraman.name}" # Signing Ultraman instance attributes
kuasa = ultraman.getKuasa() # Calling a method from Ultraman Class
warna = ultraman.getWarna()


ultraman.setWarna("Biru Hitam Emas")
warnaBaru = ultraman.getWarna()

ultraman.host = {
    "Name":"Syahmi",
    "Age": 23,
    "Gender":"Male"
}
ultraman.kaiju = ["Kaiju.1","Kaiju.2","Kaiju.3"]

# Both printed different thing because both of the meaning is different
print(ultraman.planet) # Based from the init(self) function => Instance Attributes
print(Ultraman.planet) # Based directly from Class => Class Attributes
print(name)
print(kuasa)
print(warna)
print(warnaBaru)
print(ultraman)

ultraman.kaijuInfo()
ultraman.hostInfo()
# type
# print(type(Ultraman("Ultraman Gaia",500,"Merah Putih Emas Hitam")))
# print(type(int("12")))