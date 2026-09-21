def check_prime(number):
    is_prime = False if number <= 1 else True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    return is_prime

number = int(input('Enter a number: '))
check_result = check_prime(number)
print(f"{number} is {'NOT' if not check_result else ''}a prime number")