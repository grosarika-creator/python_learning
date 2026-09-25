# *
# * *
# * * *
# * * * *
# * * * * *

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10):
    for j in range(i + 1):
        print("* ", end="")
    print()

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print("* " * i)

