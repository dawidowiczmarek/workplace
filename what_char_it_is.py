def sing_char():
    sing = ''
    while True:
        sing = input('Please get one sign...')
        if sing == 'exit':
            exit(10)

        if len(sing) == 1 and sing.isdigit():
            print(f'You entered the correct character: {sing}. That is digit')
        elif len(sing) == 1 and sing.isalpha():
            print(f'You entered the correct character: {sing}. That is alpha')
        elif len(sing) == 0:
            print(f'This is white mark! - ENTER char!')
        elif sing.isspace():  # or sing == '\n':
            print('This is white mark! - space or tab')
        elif len(sing) > 1:
            print(f'To many sign - please get one char!')
        else:
            print(f'This is a special character: {sing}')
            break

    return sing


sing_char()
