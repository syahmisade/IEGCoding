def romToNum(romNum):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romNumL = list(romNum)
    result = 0
    prevNum = 0
    
    for i in romNumL[::-1]:
        if roman_numerals[i]>prevNum:
           result +=  roman_numerals[i]
           prevNum = result
        else:
            result -= roman_numerals[i]
        

    statement = print(f"The Integer numeral is {result}")
    return statement

x = input("Enter a roman number: ").upper()
romToNum(x)