'''
A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, 
so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
Example: The quick brown fox jumps over the lazy dog.
Your task is to figure out if a sentence is a pangram.
'''
class Pangram:
        
    def __init__(self, sentence):
        self.sentence = sentence
        self.alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        self.letter = set([])   
             
    def checkLetter(self):
        for l in self.sentence:
            if l.lower() in self.alpha:
                self.letter.add(l.lower()) 
        if self.alpha == self.letter:
            return True
        else:
            return False
                
#-----------------------------------------------------------   
 
# Function: Checking if the sentence is a Pangram 
def pangram(sentence):
    
    var = Pangram(sentence)
    
    if var.checkLetter():
        return print(f"This is a pangram")
    else:
        return print(f"This is not a pangram")

def main():
    sentence = input("Enter a sentence to check if it is a Pangram or not: ")

    pangram(sentence)  
    
#----------------------------------------------------------

if __name__ == "__main__":
    main()