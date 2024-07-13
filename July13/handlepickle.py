import pickle

info = [
    {
        "product":"Television",
        "quantity":"10",
        "price":"1000"
    },
    {
        "product":"Laptop",
        "quantity":"30",
        "price":"20000"
    }
]

try:
    with open('infodatapickle.bin', 'wb') as filehandler:
        pickle.dump(info, filehandler)
except Exception as e:
    print("Something went wrong:", e)

try:
    filehandler = open('infodatapickle.bin', 'rb')
    data = pickle.load(filehandler)
    for product in data:
        print(product["product"])
        print(product["quantity"])
        print(product["price"])
except Exception as e:
    print("Something went wrong:", e)