contoh = "awdsdaef dawdsdfa dawdasda "
# x = set(contoh)
# x.remove(' ')
# print(x)

# x = ["what","is","5"]
# xstr = str(x)
# print(xstr)

example = "what is 5?".split()
x,y,z = "what","is","?"
contoh = list(example)
if x and y and z in contoh:
    contoh.remove(x)
    contoh.remove(y)
    contoh.remove(z)
else:
    print("This machine does not understand the statement")

print(contoh)