workerA = int(input("Time taken to complete project for worker A: "))
workerB = int(input("Time taken to complete project for worker B: "))

workrateA = 1/workerA
workrateB = 1/workerB

totalWorkRate = workrateA + workrateB

timeTakenTogether = 1/totalWorkRate

print(f"\nThe time taken that both workers will take to settle up a project togather: {timeTakenTogether:.2f} hours")