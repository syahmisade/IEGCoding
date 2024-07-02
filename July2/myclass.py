'''
Multiple inheritance
'''
class Card:
    def __init__(self) -> None:
        pass
    
    def doSomething(self):
        print("Register key for purchases")

class Atm(Card):
    def __init__(self) -> None:
        pass
    
    def doSomething(self):
        print("Register key for ATM")

class Debit(Card):
    def __init__(self) -> None:
        pass
    
    def doSomething(self):
        print("Register key for debit card")

class Credit(Card):
    def __init__(self) -> None:
        pass
    
    def doSomething(self):
        print("Register key for credit card")

class BankCard(Atm,Debit,Credit):
    def __init__(self) -> None:
        pass
    
    def doSomething(self):
        super().doSomething() # function super() akan ambil method based on class mana yang wujud dari kiri ke kanan
        # print("Register key for bank card")

card = BankCard()
card.doSomething()
print(BankCard.__mro__)
# (<class '__main__.BankCard'>, <class '__main__.Atm'>, <class '__main__.Debit'>, <class '__main__.Credit'>, <class '__main__.Card'>, <class 'object'>)

'''
Conclusion:
In class python:
    - def __init__():
        pass
    - def __str__():
        print(memory address)

'''

