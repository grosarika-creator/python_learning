print("IELTS BAND FEEDBACK CHECKER")

name = input("Enter your name: ")
band = float(input("Enter your IELTS overall band score: "))
weakest_skill = input(
    "Enter your weakest skill (listening/reading/writing/speaking): ").lower()

print("IELTS FEEDBACK")
print("Student:", name)
print("Overall Band:", band)

# Check IELTS band score
if band < 0 or band > 9:
    print("Invalid IELTS band score.")
elif band >= 8.5:
    print("Level: Excellent")
    print("Feedback: You demonstrate a very strong command of English.")
elif band >= 7.0:
    print("Level: Good")
    print("Feedback: You have a strong command of English, with only some mistakes.")
elif band >= 5.5:
    print("Level: Developing")
    print("Feedback: You can communicate effectively, but some areas still need improvement.")
elif band >= 4.0:
    print("Level: Needs Improvement")
    print("Feedback: You understand basic English, but you need more practice.")
else:
    print("Level: Beginner")
    print("Feedback: Focus on building your basic English skills.")

# Give feedback based on weakest skill
print("SKILL RECOMMENDATION")
match weakest_skill:
    case "listening":
        print("Practice listening to English conversations, podcasts, and IELTS recordings.")
    case "reading":
        print("Practice skimming, scanning, and identifying keywords in IELTS texts.")
    case "writing":
        print("Practice grammar, vocabulary, and organizing your ideas clearly.")
    case "speaking":
        print("Practice speaking in complete sentences and explaining your answers.")
    case _:
        print("Skill not recognized. Please choose listening, reading, writing, or speaking.")