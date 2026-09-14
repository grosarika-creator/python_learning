number = int(input('Enter a number: '))
is_prime = False if number <= 1 else True
#anggapan bahwa benar

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

# False
# 5
# cek dari 2...4

#salah
# 5 / 1 => habis (makanya is_prime = True)

# benar
# 5 / 2 => tidak habis -> is_prime = False
# 5 / 3 => tidak habis -> is_prime = False
# 5 / 4 => tidak habis -> is_prime = False

if is_prime:
    print(f"{number} is a prime number")
else: 
    print(f"{number} is not a prime number")