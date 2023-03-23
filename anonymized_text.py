text = input('Please get some text: ')
for sing in '0987654321':
    text = text.replace(sing, 'X')
print(f'Your anonymized text is: {text}')
