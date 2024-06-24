'''
Lectured by Mr.Jagen

Dictionary:
- Type of Data: 
    - DB (DataBased)
    - JSON (Javascript Object Notation)
    - XML (eXtensible Markup Language)
- Curly brackets
- Data ordered
- Data (value) is indexed by a key (not a numbers)
- Data can be duplicated, modified
- Keys:
    - Any data type can be in a key
    - The key is UNTOUCHABLE (Can only be deleted and created)
    - A key can have more than 1 data => Use list of tuple
- Square brackets hold arrays (for other language)
- Important parts in learning about DB:
    - Learn how to consume data and stored it into local DB
    - Data analysed
'''
# JSON => {}
dataBased = {
    "firstName":"Aaron",
    "lastName":"Stone",
    "passport":"SYH9087625",
    "incometaxnumber":"MY7864398",
    "pcbamount":892,
    "lastmonth":8,
    "lastyear":2024,
    "previousmonth":[(7,2024,891),(6,2024,892),(5,2024,893),(4,2024,890)], # list of tuples
    "address":{
        "office":{
            "street":"6 jalan 4/5z",
            "taman":"Tasik Cempaka"
        },
        "home":{
            "street":"0 jalan 5/67mn",
            "taman":"Taman Bakawali"
        }
    }
}

print("-"*100)
name = f"Full name: {dataBased.get("firstName")} {dataBased.get("lastName")}"
passport = f"Passport: {dataBased['passport']}"
incomeTax = f"Income tax number: {dataBased['incometaxnumber']}"
statementInfo = f"{name}\n{passport}\n{incomeTax}"
print(statementInfo)

print() # Create a gap

for i in dataBased["previousmonth"]:
    print(f"Month: {i[0]}, Year: {i[1]}, PCB Amount: {i[2]}")
    
print("-"*25 + "OR" + "-"*25) # OR
 
for month,year,pcb in dataBased["previousmonth"]:
    print(f"Transaction: {month},{year}  RM{pcb}")

print() # Create a gap

office = dataBased["address"]["office"]
home = dataBased["address"]["home"]
officeST = f"{office['street']}, {office['taman']}"
homeST = f"{home['street']}, {home['taman']}"
statementAddress = f"Office Address: {officeST}\nHome Address: {homeST}"
print(statementAddress)

print() # Create a gap

key = dataBased.keys()
print(f"List of keys: {key}")
for i in dataBased.keys():
    if isinstance(dataBased[i],list):
        for data in dataBased[i]:
            print(f"List of values: {data}")
    else:
        print(f"Value of {i}: {dataBased[i]}")

print() # Create a gap

for key,data in dataBased.items():
    print(f"Key: {key}, Data: {data}")

print() # Create a gap

dataBased["car"] = { # Can add new key and data
    "carBrand": "Toyota",
    "carModel": "Camry",
    "carYear": 2015
}
dataBased["salary"] = 4890
dataBased["salary"] = 5797 # Updating or modifies data only => change the existing "salary"

print(dataBased)

print() # Create a gap

dataBased.pop("car") # Can delete the key and data => delete "car" key
print(dataBased) # dataBased dictionary without the "car" key
