number = input("Enter a number (x to stop): ")
maximum = 0

while True: 
    if number == 'x': break
    if int(number) > maximum: maximum = int(number)
    number = input("Enter a number (x to stop): ")
print('The largest number is:', maximum)