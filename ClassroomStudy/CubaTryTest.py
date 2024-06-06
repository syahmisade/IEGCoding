# Penerangan untuk function input()
'''
umur = int(input("Umur awok berapa? "))
sentence = f"Jawapnya: Umur saya {umur} makcik"
print(sentence)

nama = int(input("Nama kau sapa?"))
print(nama)
'''
# Function for Map()
'''
a = input("Insert 3 number pls: ")
asplit = a.split()
e,f,g = map(int,asplit)
print(asplit)
print(a)
print(e,f,g)
print(type(g))
# print(type(asplit))
'''
## OR (Benda yang sama jer)
'''
e,f,g= map(int,input("Pick 3 numbers: ").split())
print(e,f,g)
print(type(g))
'''

# Format Specifier
# int  = %d
# float = %f
# str = %s
example =  3.2456
example1 = 123
example2 = "Hello"
print("%f"%example)
print("%.2f"%example)
print("%d - %.3f : %s"%(example,example1,example2))