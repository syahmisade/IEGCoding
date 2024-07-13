import mysql.connector as mysql

def keyboardInput(datatype, caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            if defaultValue is None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(connection):
    choice = -1
    while choice != 0:
        print("--------------")
        print("| 0 - Exit   |")
        print("| 1 - List   |")
        print("| 2 - Add    |")
        print("| 3 - Edit   |")
        print("| 4 - Delete |")
        print("--------------")
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be Integer")
        if choice == 0:
            print("Thank you for using our system")
            break
        elif choice == 1:
            printProduct(connection)
        elif choice == 2:
            addProduct(connection)
        elif choice == 3:
            editProduct(connection)
        elif choice == 4:
            deleteProduct(connection)

def dbConnect():
    connection = mysql.connect(
        host="localhost",
        user="root",
        password="",
        database="peneraju"
    )
    return connection

def printProduct(connection):
    SQL = "SELECT id, name, description, quantity, price FROM products"
    cursor = connection.cursor()
    cursor.execute(SQL)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':>20s}|{'Price':>20s}")
    for (id, name, description, quantity, price) in cursor:
        print(f"{id:6d}|{name:20s}|{description:40s}|{quantity:20d}|{price:20.2f}")

def addProduct(connection):
    try:
        name = keyboardInput(str, "Product Name: ", "Product Name must be String")
        description = keyboardInput(str, "Description: ", "Description must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be Integer")
        price = keyboardInput(float, "Price: ", "Price must be Float")
        SQL = "INSERT INTO products (name, description, quantity, price) VALUES (%s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(SQL, (name, description, quantity, price))
        connection.commit()
        print("Product added successfully!")
    except Exception as e:
        print("Something went wrong when adding the product:", e)

def editProduct(connection):
    try:
        product_id = keyboardInput(int, "Please enter the Product ID to edit: ", "Product ID must be Integer")
        SQL = "SELECT name, description, quantity, price FROM products WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(SQL, (product_id,))
        result = cursor.fetchone()
        if result:
            name, description, quantity, price = result
            print(f"Current details - Name: {name}, Description: {description}, Quantity: {quantity}, Price: {price}")
            new_name = keyboardInput(str, f"New Name [{name}]: ", "Name must be String", name)
            new_description = keyboardInput(str, f"New Description [{description}]: ", "Description must be String", description)
            new_quantity = keyboardInput(int, f"New Quantity [{quantity}]: ", "Quantity must be Integer", quantity)
            new_price = keyboardInput(float, f"New Price [{price}]: ", "Price must be Float", price)
            SQL = "UPDATE products SET name = %s, description = %s, quantity = %s, price = %s WHERE id = %s"
            cursor.execute(SQL, (new_name, new_description, new_quantity, new_price, product_id))
            connection.commit()
            print("Product updated successfully!")
        else:
            print("Product not found!")
    except Exception as e:
        print("Something went wrong when editing the product:", e)

def deleteProduct(connection):
    try:
        product_id = keyboardInput(int, "Please enter the Product ID to delete: ", "Product ID must be Integer")
        SQL = "SELECT name, description, quantity, price FROM products WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(SQL, (product_id,))
        result = cursor.fetchone()
        if result:
            name, description, quantity, price = result
            print(f"Current details - Name: {name}, Description: {description}, Quantity: {quantity}, Price: {price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product (y/n)? ", "Response must be string")
            if confirm.lower() == 'y': # type: ignore
                SQL = "DELETE FROM products WHERE id = %s"
                cursor.execute(SQL, (product_id,))
                connection.commit()
                print("Product deleted successfully!")
            else:
                print("Product deletion canceled.")
        else:
            print("Product not found!")
    except Exception as e:
        print("Something went wrong when deleting the product:", e)

connection = dbConnect()
doMenu(connection)
