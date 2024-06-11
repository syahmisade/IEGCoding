fruits = ["Apple","Orange","Mango","Banana","Grapes","Rambutan","Durian","Cempedak","Mangosteen"]

# List of the fruit
for fruit in fruits: # fruits[] will give fruit the contains in the list
    print(fruit) # fruit == temporary variable -> to hold the current item

print("="*50)

# List of the fruit but with step up argument
for fruit in fruits[::2]:
    print(fruit)

print("="*50)

# List of the fruit but with step up argument (reversed)
for fruit in fruits[::-1]:
    print(fruit)

print("="*50)

# List of the fruit but with if statements (6 letter only)
for fruit in fruits:
    if(len(fruit) == 6):
        print(fruit)

print("="*50)

# Printing each fruit including with the index (position)
position = 0
for fruit in fruits:
    print(position,fruit)
    position += 1