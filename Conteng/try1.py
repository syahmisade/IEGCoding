x = [23,43,65,78]
y = sorted(x)

for i in range(len(y)-1):
    if y[i] == y[i+1]:
        print("Duplicate found")
        break
    if y[-1]>y[-2]:
        print(f"Second highest {y[-2]}")
        break
