'''
Lecture by Mr.Jagen

Set: (Van Diagram)
- curly brackets {}
- modifiable and muttable
- unordered
- no duplicate values
- no indexed

'''

aSet = {10,20,30,10,20,40,50,60}
print(aSet)

for i in aSet: # Indexing and selecting
    print(i)

kasut = {"Nike","Adidas","Sketches", "Under Armor"}
print(kasut)
kasut.add("Timberland")
print(kasut)

warna = {"Merah","Biru","Kuning","Putih"}
warna.remove("Putih") # Remove specific item
warna.pop() # Random remove
print(warna)
