'''
Special Characters for String type:

\r == carriage return
\t == tab key
\f == form feed
\n == new line
\\ == backslash
f string???
'''
line = "="*50
message = '''Epul tak hensem sebab syahmi lagi hensem. 
Epul kalau \tgosok baju mesti lagi hensem\ndari sya\rhmi'''
myfile = "c:\newfolder\table\read.txt"
myfile1 = "c:\\newfolder\\table\\read.txt"
myfile2 = r"c:\newfolder\table\read.txt"

name = "Adam"
batch = 101
fstring = "F string"
fee = 325431.14124342

inputstring = f"Apa khabar {name}! Selamat datang ke kelas Python {batch}"
centerString = f"Apa khabar {name:^40}! Selamat datang ke kelas Python {batch}"
leftString = f"Apa khabar {name:<40}! Selamat datang ke kelas Python {batch}"
rightString = f"Apa khabar {name:>40}! Selamat datang ke kelas Python {batch}"
starString = f"Apa khabar {name:*>40}! Selamat datang ke kelas Python {batch}"
letterString = f"Apa khabar {name:.3}! Selamat datang ke kelas Python {batch:10d} di KL dengan harga RM{fee:10.2f}"
anotherString = f"Apa khabar {name:.3}! Selamat datang ke kelas Python {batch:b} di KL dengan harga RM{fee:10.2f}"
valueString = f"Apa khabar {name:.3}! Selamat datang ke kelas Python {batch} di KL dengan harga RM{fee:,.2f}"
example = f"Example for {fstring}:"

# {batch:o} == oktagon
# {batch:x} == heksagon 

print(example, inputstring)
print(centerString)
print(leftString)
print(rightString)
print(starString)
print(letterString)
print(anotherString)
print(valueString)

print(line)

print("Contoh:")
print(message)
print(line)
print(myfile) #ni yang salah
print(myfile1) #Ini yang betul
print(myfile2) #Ni pon betul