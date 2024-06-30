'''
Write the program to reverse the given text file.
-------------------------------------------------------------------------------------------------------
Rule:
The input file name should be input.txt and the output file name should be output.txt.
-------------------------------------------------------------------------------------------------------
Sample Input File(input.txt):
#A computer is a machine which helps us to calculate, simulate and store different scenarios. For example, in order to write an e-mail, instead of paper and pen first we use a software (or program) called wordprocessor which helps us enter sentences through keyboard (Input), computer's screen (output) to read, and modem (output/input) to send it to a distant relative, friend, etc.
-------------------------------------------------------------------------------------------------------
Sample Output File(output.txt):
.cte ,dneirf ,evitaler tnatsid a ot ti dnes ot )tupni/tuptuo( medom dna ,daer ot )tuptuo( neercs s'retupmoc ,)tupnI( draobyek hguorht secnetnes retne su spleh hcihw rossecorpdrow dellac )margorp ro( erawtfos a esu ew tsrif nep dna repap fo daetsni ,liam-e na etirw ot redro ni ,elpmaxe roF .soiranecs tnereffid erots dna etalumis ,etaluclac ot su spleh hcihw enihcam a si retupmoc A
'''


def reverseText(filename):
    inputFile = open(filename, 'r')
    outputFile = open('output.txt', 'w')
    content = inputFile.read()
    contentRev = content[::-1]
    outputFile.write(contentRev)
    inputFile.close()
    outputFile.close()


reverseText("input0.txt")
