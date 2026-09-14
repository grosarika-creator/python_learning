number = int(input('Enter a number: '))
divisible = 0

for i in range(1, number +1):
    if number % i == 0: divisible += 1

if divisible == 2:
    print(f"{number} is a prime number")
else: 
    print(f"{number} is not a prime number")