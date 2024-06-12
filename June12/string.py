'''
Lecture by Mr.Jegan

All string literals == objects
    Example:
    a = "Hello"
    a == literal/string value
    a == string object
Objects => contains function 
    function inside object == Method
        - It is possible for other data type to have their own "method" (kecuali integer)
'''
a = "Hello"
b = "Selamat pagi semua sahabat organik"
print(a.upper()) # HELLO (Example of Method)
print(a.lower()) # hello (Example of Method)
print(b.split())