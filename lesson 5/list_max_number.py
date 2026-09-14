numbers = [100, 78, 56, 88, 10, -1]

maximum = numbers[0]
for i in numbers[1:]:
    if i > maximum: maximum = i

print("Max", maximum)