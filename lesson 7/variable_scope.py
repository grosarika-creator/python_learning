name = "Joji"

def print_name():
    global name
    name = "Jack"
    print("inside fuction:", name)

print("outside fuction:", name)
print_name()
print("outside fuction:", name)