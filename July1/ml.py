'''
Encapsulation:
- A properties inside the class
- Keywords:
    - public
    - private
    - protected

'''
class circle:
    def __init__(self, radius):
        self.radius = 0 # Assign the self.radius to 0 if the input is not correct
        if isinstance(radius,int):
            self.radius = radius
        else:
            print("Radius must be an integer")
    
    # getter method and setter method
    def getRad(self):
        return self.radius
    
    def setRad(self,radius):
        if isinstance(radius,int):
            self.radius = radius
        else:
            print("Radius must be an integer")
    
    radiusInfo = property(getRad,setRad) # -> become a property
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius

myCircle = circle(12)
print(myCircle.area())
print(myCircle.circumference())
print(myCircle.radiusInfo) # -> Subtitutes for getRad()

print("-"*100)

myCircle.radiusInfo = 10 # -> Subtitutes for setRad()
print(myCircle.area())
print(myCircle.circumference())
print(myCircle.getRad())