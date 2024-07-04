'''
* Transfer pegi file atau masuk dalam list/dictionary

Car maintenance module: 
-> plat.no,car
- addting task 
- edit task
- delete task
- list task (display)
- kalau dah settle task (awaiting,in progress,completed)
- 

'''
class CarMaintenance:
    def __init__(self,plat, car):
        self.plat = plat
        self.car = car
        self.maintenance = []
        
    def addingTask(self):
        self.task = input()
        self.time = input()
        self.date = input()
        self.maintenance.append({
            "task":self.task,
            "date":self.time,
            "year":self.date
        })
        
    def display(self):
        print("Plat No: ",self.plat)

car1 = CarMaintenance("vwl2343","Toyota")