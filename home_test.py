# for n in range(1,9):
#     print('#', end=' ')
import time

# for i in range(1,3):
#     for j in range(3):
#         # i = '#'
#         # j = '$'
#         print(f"{i} {j} ", end="")
#     print()


n = int(input('Please get the number: '))
while n < 20:
    n += 1
    if n == 15:
        break
    print("end of number is: ", n)
    time.sleep(0.5)

print('------ outside of the loop --------')
