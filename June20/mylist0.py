rugby = ["prob","hooker","prob","scrumhalf","standoff","flanker","flanker","number8","inside","outside","winger","blindside"]
print(rugby.index("flanker")) # 5

newRugby = rugby[6:] # Slicing
print(newRugby)
print(newRugby.index("flanker")) # under newRugby
print(rugby.index("flanker")+1) # under rugby => flanker/item kedua yang sama nama

print(list(enumerate(rugby)))
print(list(enumerate(newRugby)))
print(enumerate(rugby)) # position dalam RAM

# enumerate returns list of tuples
for i in enumerate(rugby): # tuple => [(i[0],i[1]),...]
    # print(i[0]) # show the first object in the tupple
    # print(i[1]) # show the first object in the tupple
    # print(i) # show the tuple
    if i[1] == "flanker":
        print(f"flanker position: {i[0]}")

for i in rugby:
    if i == "flanker":
        print(f"flanker position in list rugby: {rugby.index(i)}")

print(f"Total amount of flanker: {rugby.count("flanker")}")
rugby.sort() # Ascending order from A to Z OR Integer is from small to big number
print(rugby)
rugby.reverse() # Reversed a list
print(rugby) 