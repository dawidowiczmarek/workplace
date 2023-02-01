sep = '-'
line = 40
i = ''
s = 0
n = 0
print(sep * line)
print('---- START the loop ----')
print(sep * line)

while True:
    i = int(input(f'get the number {n + 1} ...: '))
    n += 1
    if i != 0:
        s += i
        print(f'sum of before is: {s}')
        print(sep * line)

    else:
        print(sep * line)
        print(' ---- You choice => 0  ---- end of program ---- ')
        print(sep * line)
        print(f'\t \t sum of before is: {s}')
        print(sep * line)
        exit()
print('end of loop...')
