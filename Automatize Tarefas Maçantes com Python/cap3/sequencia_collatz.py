def collatz(number):
    if number % 2 == 0:
        return number // 2

    if number % 2 == 1:
        return 3 * number + 1

try:

    number = int(input('Enter number: '))
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('Por favor informe um numero inteiro!')



