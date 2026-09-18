# normal code
attempt = 0
is_guessed = False
while attempt < 3:
    if input("Enter guess: ") == "wow":
        is_guessed = True
        break
    attempt += 1
if is_guessed:
    print("You guess it right!")
else:
    print("Noway, no attempt anymore")

# syntactic sugar
attempt = 0
while attempt < 3:
    if input("Enter guess: ") == "wow":
        print("You guess it right!")
        break
    attempt += 1
else:
    print("Noway, no attempt anymore")