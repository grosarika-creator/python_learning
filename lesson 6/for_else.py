numbers = [2, 4, 6, 8, 10]

# check for odd number on a list
# normal code
is_check = False
for i in numbers:
    if i % 2 != 0:
        is_check = True
        odd = i
        break
if is_check:
    print("Odd number:", odd)
else:
    print("There's no odd number")

# syntactic sugar
for i in numbers:
    if i % 2 != 0:
        print("Odd number:", i)
        break
else:
    print("There's no odd number")