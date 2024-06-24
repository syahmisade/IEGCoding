'''
Write a program to perform basic string compression using the counts of repeated characters (e.g., "aabcccccaaa" -> "a2b1c5a3").
'''
def comString(x):
    listX = list(x)
    listSeq = []
    count = 0
    prevPos = listX[0]

    for i in listX[1:]:
        if i == prevPos:
            count += 1
        else:
            listSeq.append(prevPos + str(count + 1))
            prevPos = i
            count = 0
    
    listSeq.append(prevPos + str(count + 1))
    
    comFullStr = "".join(listSeq)
    
    return comFullStr


x = input("Enter a sequence of repeated characters: ")
result = comString(x)
print(result)

# print(listSeq)