while True:
    char = input('Please input a numeric char: ')
    if char == 'exit':
        exit(10)
    big = char.isupper()
    # print(type(big))
    # print(big)
    if char.isnumeric():
        print(f'This char ({char}) is a numeric... good work!')
    else:
        print(f'This char ({char}) is not a numeric')
    continue
