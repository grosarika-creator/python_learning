print("IELTS PRACTICE SCORE TRACKER")

score = input("Enter IELTS practice score (x to stop): ")

highest_score = 0

while True:
    if score.lower() == "x":
        break
    score = float(score)
    if score > highest_score:
        highest_score = score
    if score >= 7.0:
        print("Great job! Your score is strong.")
    elif score >= 5.5:
        print("Good progress! Keep practicing.")
    else:
        print("You still need more practice.")
    score = input("Enter IELTS practice score (x to stop): ")

print("RESULT")
print("Highest score:", highest_score)