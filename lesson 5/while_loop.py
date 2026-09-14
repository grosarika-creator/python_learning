number = '7777'
guessed_number = input('Enter your guess: ')

while guessed_number != number:
    print('Wrong guess!')
    guessed_number = input('Enter your guess: ')
print('Yey! Correct!')