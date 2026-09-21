def calculate_average(scores: list) -> float:
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

scores = [80, 90, 100, 87, 67]
average = calculate_average(scores)
print("Average:", average)