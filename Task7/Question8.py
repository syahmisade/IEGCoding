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
    def __init__(self, data=None):
        self.selectedValue = {}
        
        for key,value in data.items():  # type: ignore
          self.selectedValue[key] = { 
            "name": value["name"],
            "availableQuantity": value["availableQuantity"],
            "price": value["price"]
          }
      
    def addItem(self):
        id = input("Enter the id: ")
        name = input("Enter the name: ")
        availableQuantity = int(input("Enter the available quantity: "))
        price = float(input("Enter the price: "))
        
        self.selectedValue[id] = {
            "name": name,
            "availableQuantity": availableQuantity,
            "price": price
          }
    
    def updateItem(self,id):
        if id in self.selectedValue:
          latestN = input("Enter new name: ")
          latestAQ = int(input("Enter latest available quantity: "))
          latestP = int(input("Enter latest price: "))
          self.selectedValue[id] = {"name":latestN,"availableQuantity":latestAQ,"price":latestP}
          print(f"Completed updated {id}")
        else:
          print("Item not found")
    
    def checkItem_details(self,id):
        if id in self.selectedValue:
            print("Name:", self.selectedValue[id]["name"])
            print("Available Quantity:", self.selectedValue[id]["availableQuantity"])
            print("Price:", self.selectedValue[id]["price"])
        else:
            print("Item not found.")


def main(inventory):
  while True:
    print()
    print("1. Add item")
    print("2. Update item")
    print("3. Check item details")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
      inventory.addItem()
    elif choice == 2:
      inventory.updateItem(input("Enter an ID: "))
    elif choice ==3:
      inventory.checkItem_details(input("Enter an ID: "))
    elif choice == 4:
      print("Bye bye")
      break

if __name__ == "__main__":
  
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
  
inventory = Inventory(data)

main(inventory)
