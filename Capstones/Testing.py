'''
* Transfer pegi file atau masuk dalam list/dictionary

Car maintenance module: 
-> plat.no,car
- addting task 
- edit task
- delete task
- list task (display)
- kalau dah settle task (awaiting,in progress,completed)
-------------------------------------------------------------------------------------
Sir Jegan info:
- Maintenance Scheduling
    - Regular
    - Preventine
    - Custom Schedule
- Maintainance list
- Cars that scheduale for this day,weeks,months
- Maintenance Update
    - awaiting,in progress,completed
    - including the dates

- create car.txt (without coding)
input - processing - output
 - input -> the list of cars in txt
    - Which part have problems
- Output -> maintainance.txt

car.txt:
no.plat|brand|model|warna
- contoh: SUV2451|Honda|Civic|Black

maintenance.txt:
no.plat|problem|date|status
- contoh: SUV2451|Oiled Change|29/07/2024|In progress

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