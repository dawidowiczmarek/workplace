a = ""
n = 0
s = 0
for a in range(3):
    while True:
        a = input("Podaj liczbę: ")
        if not a.isdigit():
            print(f"'{a}' to nie jest liczba!")
        # line +=
        # a+=1
        continue
    print('end of chance - restart the program...')
    print()
