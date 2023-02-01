# your code
import random
import time
import getpass
import sys

x = random.randint(1, 100)
print("Hi there, " + getpass.getuser() + "...")
time.sleep(0.5)
print("I'm thinking of a number...")
time.sleep(0.5)
sys.stdout.flush()
y = int(input("Can you guess it?: "))
count = 0

while x != y:
    count += 1  # variable will increment every loop iteration
    print("Wrong! Ty again :)")
    time.sleep(0.25)
    if y > x:
        print("HINT: It's smaller than the number you just entered.")
    elif x > y:
        print("HINT: It's larger than the number you just entered.")
    else:
        print("Next time, please enter a number!!")
    y = int(input("Can you guess the number I am thinking of?: "))
    print("Well done, that's right!")
time.sleep(0.75)
print("It took you " + " guesses to get this correct.")
time.sleep(1.0)
print("""A token!:
     -------------------------------------
    | -50p off your next purchase at Tesco |
     -------------------------------------
      """)

print(f'to guess the number you had to make {count} runs')
