score = int(input("Enter your score: "))

if(score >= 90):
    print("Your score is A")
elif(score >= 80 and score<=89):
    print("Your score is B")
elif(score>=70 and score<=79):
    print("Your score is C")
elif(score>=60 and score<=69):
    print("Your score is D")
elif(score<60):
    print("Your score is F")
    print("Try again.")