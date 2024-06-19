'''
Create multipier of 10
Task: Do not print multipliers of 5 (10 x 5, 10 x 10)
'''
multiplication = 10
multipliers = range(1,13)
for multi in multipliers:
    if multi % 5 == 0:
        continue
    print(f"{multi} x {multiplication} = {multi*multiplication}")
