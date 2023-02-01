a = ''
count = 0
while count != 3:
    a = input('Please get the number...: ')
    if not a.isdigit():
        print(f'{a} is not a number...')
        count += 1
        continue
    break
print('---- end of chance, please turn on the program again ----')
