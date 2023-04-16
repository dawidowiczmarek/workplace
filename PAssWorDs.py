# a program to check the assumption and correctness of the entered password
while True:
    upper_yes = False
    lower_yes = False
    special_char_yes = False
    one_space = True
    enough_char = False
    digit_char = False

    password = input('Please get your password for audit...: ')
    for char in password:
        if char.isupper():
            upper_yes = True
        if char.islower():
            lower_yes = True
        if char.isspace():
            one_space = False
        if not char.isalnum():
            special_char_yes = True
        if len(password) >= 8:
            enough_char = True
        if char.isdigit():
            digit_char = True

    good_password = upper_yes and \
                    lower_yes and \
                    special_char_yes and \
                    enough_char and \
                    digit_char and \
                    one_space

    if good_password is True:
        print('This password is correct! Good work...')
        break
    else:
        print('This password is not safty... check this hint:')
    if not upper_yes:
        print('Apply upper char!')
    if not lower_yes:
        print('Apply lower char!')
    if not special_char_yes:
        print('Apply special char!')
    if not digit_char:
        print('Apply digit char!')
    if not enough_char:
        print('Apply the appropriate number of characters')
    if not one_space:
        print('Apply: company policy prohibits the use of spaces in passwords!')

print('---- END of PROGRAM -----')
