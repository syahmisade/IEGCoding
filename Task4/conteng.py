numbers = [1, 2, 3, 4, 5]

# Using a set to check for uniqueness
seen = set()
for num in numbers:
    if num in seen:
        print("Not all elements are unique.")
        break
    seen.add(num)
else:
    print("All elements are unique.")
