# you should not hardcode the data inside the program as follows
# fruits = ["apple", "orange", "mango"]
# you must keep apple, orange, mango in a txt file or csv file or excel file
# you must write a python program to read the data
# from the file and do the necessary things (print/process)
# in other words data must be seperated from the program

# You must create a file using python code
# you can use the keyword open
# open('fruits.txt')
# the open built in function takes 2 parameters
# 1) filename and 2) mode
# we have to give instruction to python if the file does not
# exist create it
# we call such extra instruction as mode
# Mode
# 1. x create the file if it does not exits
# 2. t this is going to be a text file
# 3. b this is going to be a binary file
# 4. w this will let us to write inside the file. However this will clear
# 5. a this will let us to append inside the file
#    the exisiting content inside the file.
# open('fruits.txt', 'xt')
# When we run it again we get an error and its File already exists
# we suppose to check whether the file already exists
# import os
# os.path.exists('filename')
# from os import path
# path.exists('filename')
from os.path import exists

def keyboardInput(datatype, caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1
    while (choice != 0):
        print("--------------")
        print("| 0 - Exit   |")
        print("| 1 - List   |")
        print("| 2 - Add    |")
        print("| 3 - Edit   |")
        print("| 4 - Delete |")
        print("--------------")
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be Integer")
        if (choice == 0):
            print("Thank you for using our system")
            break
        elif (choice == 1):
            printProduct(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)
        elif (choice == 4):
            deleteProduct(filename)

# if exists(filename):
#    pass
# else:
#    open(filename, 'xt')
def createFile(filename):
    if not exists(filename):
        try:
            # the open built in function open the file and return the handler
            # which we can use to read / write inside the file
            # filehandler is an object/instance of File Class
            filehandler = open(filename, "xt")
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
            createTitle(filename)
        finally:
            # filehandler has many methods like read, write and close
            filehandler.close()

# whenever you come out of with block the resource will be closed automatically
def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            # here | (pipe) is used as delimiter
            # we can use delimiter to split the line into
            # multiple data
            # "Television201455.55"
            # "Television|20|1455.55"
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
        print("Something went wrong when we create the header:", e)

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be Integer")
        price = keyboardInput(float, "Price: ", "Price must be Float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def printProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if (index == 0):
                print(f"{"No.":5}{product:40}{quantity:>20}{price:>20}")
                print("=" * 85)
            else:
                print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something went wrong when we print the products:", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please keyin index of the Product: ", "Index must be Integer")
        if (index >= len(data)): # type: ignore
            print("Sorry product not available")
        else:
            product, quantity, price = data[index] # type: ignore
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to edit this product (y/n) ?", "Response must be string")
            if (confirm == 'y'):
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be String", product)
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be Integer", quantity)
                newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be Float", price)
                data[index] = [newproduct, newquantity, newprice] # type: ignore
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the products:", e)

def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please keyin index of the Product: ", "Index must be Integer")
        if (index >= len(data)): # type: ignore
            print("Sorry product not available")
        else:
            product, quantity, price = data[index] # type: ignore
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product (y/n) ?", "Response must be string")
            if (confirm == 'y'):
                del data[index] # type: ignore
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we edit the products:", e)

filename = "sirjagen.txt"
createFile(filename)
doMenu(filename)
# addProduct(filename)
# printProduct(filename)





