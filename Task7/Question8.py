'''
Write a Python class Inventory with attributes like id, productName, availableQuantity and price. 
Add methods like addItem, updateItem, and checkItem_details.
Use a dictionary to store the item details, where the key is the id and the value is a dictionary containing the productName, 
availableQuantity and price.
Sample Data:
{
  "97410": {
    "name": "Television",
    "availableQuantity": 20,
    "price": 1455.99
  },
  "97411": {
    "name": "Radio",
    "availableQuantity": 32,
    "price": 654.25
  }
}
'''
class Inventory:
    def __init__(self, id, name, availableQuantity, price):
        self.id = id
        self.name = name
        self.availableQuantity = availableQuantity
        self.price = price
        
    def addItem(self, id, name, availableQuantity, price):
        pass
    
    def updateItem(self):
        pass
    
    def checkItem_details(self):
        pass

data = {
  "97410": {
    "name": "Television",
    "availableQuantity": 20,
    "price": 1455.99
  },
  "97411": {
    "name": "Radio",
    "availableQuantity": 32,
    "price": 654.25
  }
}


