'''
File focus: Xclusive only
'''
file = open("try.txt",
            "x")
# kalau kita letak nama file yang dah memang ada dalam folder, kita akan dapat error


text = "Contoh saja saja jer nii\n"
textlagi = "Contoh lagi satu kalau nak try\n"
textline = ["Google\n", "Amazon\n", "Apple\n",]
file.write(text)
file.write(textlagi)
file.writelines(textline)
