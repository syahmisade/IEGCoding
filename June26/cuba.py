class CarMaintenance:
    def __init__(s,plat,car,model):
        s.nombor = plat
        s.car = car
        s.maintenance = []
        
    def __str__():
        pass    
        
    def addingTask(s):
        s.task = input("Add task: ")
        s.time = input("Add time: ")
        s.date = input("Add date: ")
        s.maintenance.append({
            "task":s.task,
            "date":s.time,
            "year":s.date
        })
        # print()
        # print(s.maintenance)
        # print()
    
    def displayList(s):
        print(s.maintenance)
    
    def display(s):
        print("Plat No: ",s.nombor)
        
def plus(a,b):
    return a+b # value
    return print(a+b) # display value

a = 1
b = 2

# print(plus(a,b) + b)
plus(a,b)

