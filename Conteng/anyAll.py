users_data = [
    {
        "name": "adam",
        "location": "bangi"
    },
    {
        "name": "anith",
        "location": "terengganu"
    }
]
mylocation = input("Location: ")
membernear = [i for i in users_data if i["location"] == mylocation]

# if len(membernear) > 0:
#     # print("There are {} members near you".format(len(membernear)))
#     print(f"There are {len(membernear)} members near you")

if any(membernear):  # False if empty, True if at least 1
    print(f"There are {len(membernear)} members near you")

print(all([0, 1, 2, 3, 4, 5]))  # False if there is 0 in and iteration
