import json

try:
    with open("dictfile.json", "r") as filehandler:
        data = json.load(filehandler)
        
    for product in data:
        print(product)
except Exception as e:
    print(f"Something when wrong gilak: {e}")