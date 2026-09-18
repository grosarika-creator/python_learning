numbers = [2, 4, 6, 5, 10]

# check for odd number on a list
# normal code
is_odd = False
for i in numbers:
    if i % 2 != 0:
        is_odd = True
        odd = i
        break
if is_odd:
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