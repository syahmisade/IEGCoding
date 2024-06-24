'''
Lectured by Mr.Jagen
- A way to demonstrate the feature of a data structure
- 
'''
emailcontent = '''Your subject line will be the single most important element in your formal email writing. 
It is the first thing your recipient will see, so your goal here is to convince them that your email is a safe, relevant, and high priority (in that order). 
If you do not succeed in doing that, your email may never be opened, and any effort you put into the rest of the email elements will go to waste.'''

words = emailcontent.split()

uniqueW = set(words)

commonW = {"is","of","so","the","by","it","when","how","into","in","are","your","you","i","to"}

unique = uniqueW.difference(commonW)

cleanW = []
for i in words:
    i = i.replace(",", "")
    i = i.replace(".", "")
    i = i.replace("(","")
    i = i.replace(")","")
    i = i.lower()
    cleanW.append(i)
    
print(f"- The length of the words are {len(words)}")
print(f"- The length of the unique words are {len(uniqueW)}")
print(f"- Display the clean words: {cleanW} => Total words: {len(cleanW)}")
print("-"*150)
print(f"- The words without comment words: {unique} => Total words: {len(unique)}")