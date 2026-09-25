# IELTS PROGRESS CHECKER

print("IELTS PROGRESS CHECKER")

def give_band_feedback(band):
    if band < 0 or band > 9:
        return "Invalid IELTS band score."
    elif band >= 8.5:
        return "Excellent! You demonstrate a very strong command of English."
    elif band >= 7.0:
        return "Good! You have a strong command of English."
    elif band >= 5.5:
        return "Developing. You are making good progress."
    elif band >= 4.0:
        return "Needs Improvement. Keep practicing."
    else:
        return "Beginner. Focus on building your basic English skills."

def give_skill_recommendation(skill):
    skill = skill.lower()

    match skill:
        case "listening":
            return "Practice listening to English podcasts and IELTS recordings."
        case "reading":
            return "Practice skimming, scanning, and identifying keywords."
        case "writing":
            return "Practice grammar, vocabulary, and organizing your ideas."
        case "speaking":
            return "Practice speaking in complete sentences and explaining your answers."
        case _:
            return "Skill not recognized."

def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    return total / len(scores)

name = input("Enter your name: ")

listening = float(input("Enter Listening score: "))
reading = float(input("Enter Reading score: "))
writing = float(input("Enter Writing score: "))
speaking = float(input("Enter Speaking score: "))

weakest_skill = input(
    "Enter your weakest skill (listening/reading/writing/speaking): "
)

scores = [listening, reading, writing, speaking]

average = calculate_average(scores)

print("IELTS RESULT")
print("Student:", name)
print("Average Score:", average)
print("Feedback:", give_band_feedback(average))

print("SKILL RECOMMENDATION")
print(give_skill_recommendation(weakest_skill))