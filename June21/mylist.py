ultraman = ["Gaia","Agul","Dyna","Tiga","Taro","Seven","Zero"]
y = ultraman # Dont do like this
ultraman[2] = "Mebius"
print(y)
print(ultraman)

print("="*50)

ultraman = ["Gaia","Agul","Dyna","Tiga","Taro","Seven","Zero"]
y = []
for i in ultraman: # Do it like this
    y.append(i)
ultraman[2] = "Mebius"
print(y)
print(ultraman)

print("="*50)

ultraman = ["Gaia","Agul","Dyna","Tiga","Taro","Seven","Zero"]
y = ultraman.copy() # Do it like this
ultraman[2] = "Mebius"
print(y)
print(ultraman)

print("="*50)

# Technically, this is the way to return a list but python can use square brackets
ultraman = list(["Gaia","Agul","Dyna","Tiga","Taro","Seven","Zero"])
print(ultraman)

musimList = ["Salji","Panas","Bunga","Luruh"]

musim01 = musimList[0]
musim02 = musimList[1]
musim03 = musimList[2]
musim01,musim02,musim03 = musimList
