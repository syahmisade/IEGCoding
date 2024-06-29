'''

'''
file = open("contoh.txt", "wt")

# Text akan terdelete kalau ada text lain yang ganti
# (kalau serentak, baru tak ada yang terdelete)
text = "Contoh saja saja jer nii\n"
textlagi = "Contoh lagi satu kalau nak try"
file.write(text)  # Susunan mana satu nak .write() tu penting
file.write(textlagi)
