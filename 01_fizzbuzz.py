# # fizz buzz

for n in range(1,21):
    if n % 3 == 0 and n % 5 == 0:
        print( 'FIZZBUZZ ')
    elif n % 5 == 0:
        print( 'BUZZ')
    elif n % 3 == 0:
        print( 'FIZZ')
    else:
        print(n)