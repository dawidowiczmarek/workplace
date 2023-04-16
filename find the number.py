import random

print('Guess the number !')
b = random.randint(1, 100)
while True:
    n = 0
    for n in range(1, 21):
        p = n + 1
        a = int(input('Please choice the number between 1 - 100! : '))
        if b > a:
            print(f'Yours choice number is too little! Please choice different number!')
        elif b < a:
            print('Yours choice number is too many! Please choice different number!')
        else:
            print(f'You made {p} choices!')
            print(f'Yours choice number: {a} is correct! Excellent choice!')
            exit(11)
