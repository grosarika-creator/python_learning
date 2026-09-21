scores = [1, 2, 3, 4, 5]

def sum_score(scores):
    if len(scores) == 0:
        return 0
    return scores[0] + sum_score(scores[1:])

print("Sum:", sum_score(scores))