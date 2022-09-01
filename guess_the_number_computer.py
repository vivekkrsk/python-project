import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while int(guess) != random_number:
        guess = input(f"Guess a number between 1 and {x}: ")
        #print(guess)
        if int(guess) < random_number:
            print("Sorry, guess again. Too low")
        elif int(guess) > random_number:
            print("Sorry, guess again. Too high")

    print(f"Yay, congratulation. You have Guessed the number {random_number} correctly")

guess(10)
