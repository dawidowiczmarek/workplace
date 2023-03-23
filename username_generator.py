import re

s = '-'
b = '_'
line = 50
print(s * line)
print('USERNAME_GENERATOR')
print(s * line)
name = ''
surname = ''
while True:
    name = input('Please get your name: ')
    surname = input('Please get your surname: ')
    if len(name) == 0:
        print('!!! ---- expression is empty, write an expression ---- !!!')
    elif name.isspace():
        print('!!! ---- yours char is a white space ---- !!!')
    elif len(name) != 0:
        print('     ---------- S O L U T I O N ---------- ')
        sname = name.lower().lstrip().rstrip().replace(' ', b)
        ssurname = surname.lower().lstrip().rstrip()
        print(f'{sname.upper()[0]}. {ssurname.upper()[0]}.')
        break
