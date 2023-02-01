a=''
counter = 0
while counter != 3:
    a = input('get the number...: ')
    counter += 1
    if a.isdigit():
        print(f'you entered sing: {a} ')

        exit('---end OF program---')
    else:
        print(f'{a} is not a number...')

print('---- end of chance, please turn on the program again ----')
