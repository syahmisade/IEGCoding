# List -> containt index [0,1,2,3,...]
fruits = ["Apple","Orange","Mango","Banana","Grapes","Rambutan","Durian","Cempedak","Mangosteen","Jagung"]

print(f"The list of fruits: {fruits}")
print("-"*50)
print(f"The first fruit in the list: {fruits[0]}")
print(f"The forth fruit in the list: {fruits[3]}")
print(f"The number of items we have: {len(fruits)}")
print(f"The maximum index: {len(fruits) - 1}")
print(f"The -1 index: {fruits[-1]}")
print(f"The -3 index: {fruits[-3]}")
print(f"I like {fruits[1:4]}")
print(f"I also like {fruits[:2]}")
print(f"but I love {fruits[1:]}")
print(f"Now I love {fruits[0:9]}")
print(f"But my most likeble fruits are {fruits[0:9:3]}") # list[index:index:(step up argument)]
print(f"I also eat {fruits[-5:-1]}")
print(f"I also want eat {fruits[-1:-5:-1]}") # -1>-5, so you need to add -1 as a step up argument
print(f"The reverse list of fruits is {fruits[::-1]}") # Reversing the list 