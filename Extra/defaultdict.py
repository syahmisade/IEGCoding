from collections import defaultdict

print("Example for defaultdict:")
student = [
    ("adam", "UM"), ("syahmi", "sheffield"), ("najmi", "korea")
]

# dictionary: kalau key tu tak ada dalam dictionary ni, dia akan return list kosong
studentDict = defaultdict(list)

for name, place in student:
    studentDict[name].append(place)

studentDict.default_factory = None

try:
    print(studentDict["adam"])
    print(studentDict["mun"])
except KeyError:
    print("Key not found")

# another example --------------------------------------------------------
mycompany = "Tesco"
coworker = ["adam", "najmi", "naja", "hadi"]
otherCW = [("billy", "Giant"), ("lara", "Apple")]

# dictionary: kalau value ndak ada, dia akan return "Tesco"
coworkerCompany = defaultdict(lambda: mycompany)

for worker, company in otherCW:
    coworkerCompany[worker] = company

print(coworkerCompany["adam"])
print(coworkerCompany["billy"])
