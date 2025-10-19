import random

lowest_num = 1
highest_num = 100
num = random.randint(lowest_num, highest_num)
guess = input(f"Guess a number between {lowest_num} and {highest_num}: ")
guesses = 0
is_running = True


while is_running:

    if not guess.isdigit():
        print(f"'{guess}' is not valid! ")
        guess = input("Please guess a NUMBER between 1 and 10: ")
    elif int(guess) < lowest_num or int(guess) > highest_num:
        print(f"{guess} is out of range!")
        guess = input("Please guess a number only between 1 and 10: ")
    elif int(guess) > num:
        print("too high!")
        guess = input("Try again: ")
        guesses += 1
    elif int(guess) < num:
        print("too low!")
        guess = input("Try again: ")
        guesses += 1
    else:
        print("--------------CORRECT--------------")
        print(f"{guess} is the correct number!")
        print(f"You toke {guesses} valid guesses.")
        is_running = False
