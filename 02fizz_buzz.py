f = 'Fizz'
b = 'Buzz'
fb = 'Fizz Buzz'

for n in range(1,21):
    if n % 3 == 0 and n % 5 == 0:
        print(n, fb)
    elif n % 5 == 0:
        print(n, b)
    elif n % 3 == 0:
        print(n, f)
    else:
        print(n, end="\n")