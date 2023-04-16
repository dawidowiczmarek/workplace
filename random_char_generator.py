import random

print('---- Lotto numbers generator ----')
print(f'Random 5 of 50 numbers:')
# for a in range(1, 6):
for b in range(1, 6):
    print(f'{b} of number:', random.randint(1, 51))

print(f'Random 2 of 12 numbers:')
for r in range(1, 3):
    print(f'{r} of number:', random.randint(1, 13))
# print(random.randint(1,100))

print('Guess the number!')
# for a in range(1,101):
a = int(input('Please choice the number! : ')))
b = random.randint(1, 100)
if b > a:
    print(f'Yours choice number is too short! Please choice different number!')
print(int(input('Next number: '))
elif b < a:

# print('')
