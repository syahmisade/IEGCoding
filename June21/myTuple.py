'''
Lecture by Mr.Jegan

Tuple:
- read only list
- uses ()
- immutable (not modifiable)
- ordered
- indexed
- can duplicates (.copy)
- can be count (count any duplicates)
- can assign many item in the tuple into many variables
'''
musim = ("Salji","Panas","Bunga","Luruh")
musimList = ["Salji","Panas","Bunga","Luruh"]
print(musim)
print(type(musim))

musim = tuple(musimList)

musim01 = musim[0]
musim02 = musim[1]
musim03 = musim[2]
#musim01,musim02,musim03 = musim # can be explode directly in the same time

x = (10)
print(type(x),x)

x = (10,)
print(type(x),x)