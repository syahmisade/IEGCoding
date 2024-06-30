'''
file focus: Append only
'''
file = open("test.txt",
            "a")
# kalau "a" ni kita tukar jadi "w", nnt die akan padam append text semua and
# re-do balik as write file and bukan append file


text = "Contoh saja saja jer nii\n"
textlagi = "Contoh lagi satu kalau nak try\n"
textline = ["Google\n", "Amazon\n", "Apple\n",]
file.write(text)
file.write(textlagi)
file.writelines(textline)
