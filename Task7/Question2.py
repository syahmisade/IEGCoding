'''
An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, 
however spaces and hyphens are allowed to appear multiple times.
Examples of isograms:
lumberjacks background downstream six-year-old
The word isograms, however, is not an isogram, because the s repeats.
Your task is to figure out if the user input is isogram
'''

# class Isogram: # Class
#     def __init__(self, sentences): # Initialization
#         self.sentences = sentences
#         self.isogram = True
    
#     def originalSentences(self):
#         self.sentences = self.sentences.lower()
#         self.sentences = self.sentences.replace(" ", "")
#         self.sentences = self.sentences.replace("-", "")
#         return self.sentences
    
#     def convertSentence(self):
#         setOfWords = set(self.originalSentences())
#         return setOfWords
    
#     def is_isogram(self):
#         self.isogram = len(self.originalSentences()) == len(self.convertSentence())
#         return self.isogram

# def checkingIsogram(sentence):
    
#     data = Isogram(sentence)
#     if data.is_isogram():
#         print("The sentence is an isogram")
#     else:
#         print("The sentence is not an isogram")
    

# def main():
#     sentence = input("Enter a sentence: ")
#     checkingIsogram(sentence)
    
# if __name__ == "__main__":
#     main()

class Isogram:  # Class
    def __init__(self, sentences):  # Initialization
        self.sentences = sentences
        self.isogram = True

    def originalSentences(self):
        self.sentences = self.sentences.lower()
        self.sentences = self.sentences.replace(" ", "")
        self.sentences = self.sentences.replace("-", "")
        return self.sentences
    
    def convertList(self):
        listOfWords = list(self.originalSentences())
        return listOfWords

    def convertSentence(self):
        setOfWords = set(self.convertList())
        return setOfWords

    def is_isogram(self):
        self.isogram = len(self.convertList()) == len(self.convertSentence())
        return self.isogram

def checkingIsogram(sentence):
    data = Isogram(sentence)
    if data.is_isogram():
        print("The sentence is an isogram")
    else:
        print("The sentence is not an isogram")

def main():
    sentence = input("Enter a word/s or sentence/s to check if it is Isogram: ")
    checkingIsogram(sentence)

if __name__ == "__main__":
    main()

