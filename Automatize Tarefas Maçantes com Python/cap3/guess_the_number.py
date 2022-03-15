# Este é um jogo de adivinhar o número
import random

secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Peça para o jogador adivinhar 6 vezes.
for guess_taken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('You guess is too low.')
    elif guess > secret_number:
        print('You guess is too high')
    else:
        break # Esta condição corresponde ao palpite correto!

    if guess == secret_number:
        print('Good job! You guessed my number in ' + str(guess_taken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number))


