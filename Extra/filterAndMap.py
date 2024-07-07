def customFilter(func, iter):
    for i in iter:
        if func(i):
            yield i


exampleIter = ["Kroos", "Benzema", "Ronaldo", "Bale", "rodrigo", "Isco"]
print("\nExample of customFilter: ")
print(list(customFilter(lambda x: x[0].isupper(), exampleIter)))
print(list(customFilter(lambda x: x[0] == "R" or x[0] == "r", exampleIter)))
print(f"{exampleIter}")

print("\nExample of map(): ")
lowerIter = map(lambda x: x.lower(), exampleIter)
print(list(lowerIter))
# -----------------------------------------------


class User:
    def __init__(self, username, password):
        self.un = username
        self.pw = password

    @classmethod
    def fromDict(cls, data):
        return cls(data["username"], data["password"])


users_data = [
    {
        "username": "adam",
        "password": "adamnayel123"
    },
    {
        "username": "anith",
        "password": "anithcantik123"
    }
]

# Using list comprehension to create a list of User objects
# users = [User.fromDict(user) for user in users_data]

# Alternatively, using map to create an iterator of User objects
users_iter = map(User.fromDict, users_data)

# Iterating over the users list or users_iter iterator
for user in users_iter:
    print(f"Username: {user.un}, Password: {user.pw}")
