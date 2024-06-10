'''
Special Characters for String type:

\r == carriage return
\t == tab key
\f == form feed
\n == new line
\\ == backslash
f string???
'''

message = '''
Epul tak hensem sebab syahmi lagi hensem. 
Epul kalau \tgosok baju 
mesti lagi hensem\ndari sya\rhmi
'''
myfile = "c:\newfolder\table\read.txt"
myfile1 = "c:\\newfolder\\table\\read.txt"
myfile2 = r"c:\newfolder\table\read.txt"

print(message)
print(myfile)
print(myfile1)
print(myfile2)