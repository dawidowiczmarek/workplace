passchar = input('Please write Yours PASSWORD: ')
for s in passchar:
    if s.isdigit():
        print(f'{s} is digit')
    elif s.isalpha():
        print(f'{s} is alpha')
    elif s.isspace():
        print(f'{s} is white sing')
    else:
        print(f'{s} is special sing')
print(passchar)
