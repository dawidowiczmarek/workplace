# i = 0
# while i < 10:
#     i +=1
#     print(i)
a = ''
while not a.isdigit():
    a = input('Podaj a:')

b = ''
while not b.isdigit():
    b = input('Podaj b:')
a = int(a)
b = int(b)

print(f'{a }+{b }={a + b}')
