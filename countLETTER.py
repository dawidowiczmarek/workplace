#  zliczanie liter i znaków we wprowadzonym tekscie

count = 0
text = input('Pleas enter some text: ')
for sing in text:
    if sing.isalpha():
        count += 1
print(f'This text has {count} letters and', len(text), 'sing.')
