#  pętla która wczytuje liczby i dodaje je do siebie do momtnu aż użytkownik wpisze 0
# ----------------------------------------------------------------------------------------------
sep = '-'
line = 60
s = 0
while True:
    i = int(input(f'Please get the number: '))
    if i == 0:
        break
    s += i
print(sep * line)
print('the sum of all operations is: ', s)
print(sep * line)
print('-------- end of the program ---------')
print(sep * line)
# -------------------------------------------------------------------------------------------------
