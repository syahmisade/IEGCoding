from collections import namedtuple


acc = ("checking", 1545)
# print(acc[0])
# print(acc[1])
Account = namedtuple("Account", ["name", "balance"])  # Class copy ori

account = Account("checking", 1000)
# accNamedTuple = Account._make(acc) # Same as line below
accNamedTuple = Account(*acc)

exampleDict = accNamedTuple._asdict()

print(account.balance)
print(account)
print(accNamedTuple)
print(exampleDict)
print(exampleDict["balance"])
