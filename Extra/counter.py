from collections import Counter

print("Example for Counter:")
devTemps = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

tempcounter = Counter(devTemps)
print(tempcounter)
print(tempcounter[14.0])
