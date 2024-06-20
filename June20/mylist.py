'''
List []:
- modifiable (append,edit,delete)
- ordered (the item retained its position)
- indexed (0,1,2,3,4,...)
- duplicates

'''
# Each ultraman in the list is called Object => instance of a class
# Gaia,Agul,Dyna,Tiga are objects, instance of Ultraman Class
# Gaia has bright eyes, light on chest, hands(2),leg(2) => Properties
# Gaia can run, jump, shoot => Methods
ultraman = ["Gaia","Agul","Dyna","Tiga","Taro","Seven","Zero"]
ultraman.append("Mebius") # Append into ultraman[-1]
ultraman.insert(1,"Hikari") # Insert into ultraman[1]
ultraman.insert(5,"Jack") # Insert into ultraman[5]
ultraman.insert(7,"Belial") # Insert into ultraman[7]
ultraman[7] = "Geed" # Updating into ultraman[7]
ultraman.remove("Taro") # Remove Taro from ultraman
ultraman.pop() # Remove the last item in ultraman[]
del ultraman[1] # Remove the object in ultraman[1]

print(ultraman)

ultraman.clear()
# OR
# del ultraman => will delete the list entirely 
print(ultraman)
