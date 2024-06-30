'''
File focus: Write only
'''
file = open("contoh.txt",
            "wt")  # asalnya contoh.txt ni tak wujud pon dalam folder ReadFile

# Text akan terdelete kalau ada text lain yang ganti
# (kalau serentak, baru tak ada yang terdelete)
text = "Contoh saja saja jer nii\n"
textlagi = "Contoh lagi satu kalau nak try\n"
textline = ["Google\n", "Amazon\n", "Apple\n",]
file.write(text)  # Susunan mana satu nak .write() tu penting
file.write(textlagi)
file.writelines(textline)
