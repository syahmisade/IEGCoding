x = 4
y = 4

print(x+y)

# Penghadang supaya tak confius maa
print(" ")
print("#######################################################")
print(" ")

# From Mr.Jegan ##################################################################
# print => python build in function
# will get help from windows to print the output in the monitor (output device)
# when you call a function, must be followed by ()
# in (), we will have n numbers of arguments
###################################################################################

print("Welcome to python guys!!!") # 1 function, 1 arguments
print("Nasi lemak","Teh ais") # 1 function, 2 arguments

print(" ")
print("#######################################################")
print(" ")

# function => arahan yang dipendekkan, tak payah cakap panjang2, cakap simple2 jer
# Contoh => Belikan makanan, tak perlu cakap tapau kan elok2 letak dalam bekas bagai
# argument => apa yang nak difocuskan based on the function
# Contoh (daripada contoh tadi) => Nasi goreng ayam dengan teh ais ikat tocang (2 arguments)

# From Mr.Jegan ##################################################################
# product is a variable
# Television is the string value/literal
# To differentiate the variables from values => "" OR ''
#################################################################################

product = "Television" # string
quantity = 2 # integer
price = 1000.50 # float
available = True # booleanvalue/literal
print("Product:",product)
print("Quantity:",quantity)
print("Price:",price)
print("Availability:",available)

print(" ")
print("#######################################################")
print(" ")

# From Mr.Jegan ##################################################################
# type is another build in function that tell us what is the data type of the variables
# (Dynamically assigned by python)
##################################################################################
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

print(" ")
print("#######################################################")
print(" ")

# Always remember this: BODMAS
a=1
b=2
c=3
z = (a + b) / c
print(z)

print(" ")
print("#######################################################")
print(" ")

# From Mr.Jegan ################################################################
# Variables will always dynamically Typed Programming Language
# Python is dynamically typed programming language
################################################################################

totalPrice = quantity * price
print("Total: ",totalPrice)

quantityString = "10"
print(type(quantityString))

# Cannot recive result because the variables have different data types
# result = quantityString * price
# print(result)

# From Mr.Jegan ################################################################
# Type casting
# Convert one data type into another data type
# To convert string to integer => using build in function int
################################################################################

result = int(quantityString) * float(price)
print(result)

#################################################################################