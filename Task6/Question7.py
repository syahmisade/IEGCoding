'''
Write a python function that takes 2 parameters lower and upper (range). Let the function returns pairs of amicable numbers in that range.
Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal to the other number. 
For example 220 and 284 are amicable numbers.
For example if we call that function: amicableNumbers(1, 1000)
The function must return: [220, 284]
Why they are amicable numbers ?
Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284
Sum of proper divisors of 284 = 1+2+4+71+142 = 220
'''
def amicable(lower,upper):
    
    def totalDivisor(i):
        sumDiv = 0
        for j in range(1,i):
            if i%j == 0:
                sumDiv += j
        return sumDiv
    
    listAmicable = []
    
    for i in range(lower,upper+1):
        sumDiv = totalDivisor(i)
        if sumDiv > i:
            sumDiv2 = totalDivisor(sumDiv)
            if sumDiv2 == i and sumDiv != sumDiv2:
                listAmicable.append(i)
                listAmicable.append(sumDiv)
    return listAmicable

print(amicable(1,1000))
