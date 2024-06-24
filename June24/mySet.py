'''
Lectured by Mr.Jegan
'''

negeri = ["Selangor","Sabah","Kelantan","Pahang","Perak","Perak","Sarawak","Sabah"]
negeriSet = set(negeri)
negeriList = list(negeriSet)

print(f"Negeri : {negeri}")
print(f"Negeri Set : {negeriSet}")
print(f"Negeri List : {negeriList}")

setA = {10,20,30,40,50,60}
setB = {10,20,30,70,80,90}

# .difference()
print(setA.difference(setB)) # Kita ambik baki setA (setA - setB)
print(setB.difference(setA)) # Kita ambik baki setB (setB - setA)

# .issubset()
print(setA.issubset(setB)) # False
print(setB.issubset(setA)) # True

#.issuperset()
print(setA.issuperset(setB)) # True
print(setB.issuperset(setA)) # False

# .union() & .intersection()
print(setA.union(setB)) # Gabungan setA dan setB
print(setA.intersection(setB)) # Kita ambik elemen yang sama dalam setA dan setB SAHAJA!

setC = {20,40,70}

print(setC.issubset(setA)) # False sbb walaupun 2 num setC ada dalam setA, TAPI kene semua num setC ADA dalam setA baru lah True

print(setC.isdisjoint(setB)) # False sbb walaupun 2 num setC tak ada dalam setB, TAPI kene semua num setC TAK ADA dalam setB baru lah True