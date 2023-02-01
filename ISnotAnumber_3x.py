a = ''
count = 0
while count < 3:
    a = input('get the number...: ')
    count += 1
    if a.isdigit() and len(a) == 1:
        print(f'Your choice: {a} is a digit and one char')
        exit('---- end of program ----')
    elif count == 3:
        print('---- end of program: you entered the wrong value three times... ----')
    else:
        print('!!! ---- expression is wrong, write the correct expression ---- !!!')
