number1 = int(input('Input number 1: '))
number2 = int(input('Input number 2: '))
number3 = int(input('Input number 3: '))

maximum = 0
if number1 >= number2:
    if number1 >= number3:
        maximum = number1
    else:
        maximum = number3
else:
    if number2 >= number3:
        maximum = number2
    else:
        maximum = number3

print("Max", maximum)