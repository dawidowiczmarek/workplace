s = '-'
b = '_'
line = 50
print(s * line)
print('     ---------- ONE CHAR CHECK --------- ')
print(s * line)
name = ''
while True:
    name = input('Please get one char...:')
    if len(name) != 1:
        print('!!! ---- expression is wrong, write the correct expression ---- !!!')
    elif name.isspace():
        print('Yours sing is a white sing...')
    else:
        print(s * line)
        print('     ---------- S O L U T I O N ---------- ')
        print(f' Your char is " {name} " - well done...')
        exit()