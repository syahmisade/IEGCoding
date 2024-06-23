'''
Write a program that converts a number to its word representation (e.g., 123 to "one hundred twenty-three").
'''
def number_to_words(n):

    def satuDigit(num):
        nums = {
            1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
        }
        return nums.get(num, '')

    def digitBelas(num):
        nums = {
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }
        return nums.get(num, '')

    def digitPuluh(num):
        nums = {
            20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty', 90: 'ninety'
        }
        return nums.get(num, '')

    def duaDigit(num):
        if not num:
            return ''
        elif num < 10:
            return satuDigit(num)
        elif num < 20:
            return digitBelas(num)
        else:
            puluh = num // 10 * 10
            baki = num % 10
            return digitPuluh(puluh) + ('-' + satuDigit(baki) if baki else '')

    def tigaDigit(num):
        hundred = num // 100
        baki = num % 100
        if hundred and baki:
            return satuDigit(hundred) + ' hundred ' + duaDigit(baki)
        elif not hundred and baki:
            return duaDigit(baki)
        elif hundred and not baki:
            return satuDigit(hundred) + ' hundred'
        else:
            return ''

    ribu = n // 1000
    baki = n % 1000

    if n == 0:
        return "zero"

    if ribu and baki:
        return tigaDigit(ribu) + ' thousand ' + tigaDigit(baki)
    elif not ribu and baki:
        return tigaDigit(baki)
    elif ribu and not baki:
        return tigaDigit(ribu) + ' thousand'
    else:
        return ''

number = int(input("Enter a number: "))
print(number_to_words(number))