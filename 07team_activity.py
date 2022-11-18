import random

magic_number = random.randint(1,100)

number = 0

while number != magic_number:
    number = int(input("Guess the magic number: "))
    if number < magic_number:
        print("Guess higher.")
    elif number > magic_number:
        print("Guess lower.")
    elif number == magic_number:
        print("You guessed correctly! ")