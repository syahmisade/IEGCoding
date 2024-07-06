'''
Write a Python class BankAccount with attributes like accountNumber, openingBalance, currentBalance dateOfOpening and 
customerName. Add methods like deposit, withdraw, and checkBalance.
'''


class BankAccount:
    def __init__(self, accountNumber, openingBalance, currentBalance, dateOfOpening, customerName):
        self.aN = accountNumber
        self.oB = openingBalance
        self.cB = currentBalance
        self.dO = dateOfOpening
        self.cN = customerName

    def deposit(self, amount):
        self.cB = self.cB+amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount > self.cB:
            print("Insufficient balance")
        else:
            self.cB = self.cB-amount
            print("Amount withdrawn successfully")

    def checkBalance(self):
        print("Current balance is", self.cB)


mayban = BankAccount(123456789, 10, 1000, 12/12, "Abu")
mayban.deposit(100)
mayban.withdraw(1000)
mayban.checkBalance()
