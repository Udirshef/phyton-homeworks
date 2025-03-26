import random

while True:
    number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. You have 10 attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it right!")
            break

        attempts -= 1

    if attempts == 0:
        print(f"You lost. The correct number was {number}.")

    play_again = input("Want to play again? (Y/YES/y/yes/ok): ").strip().lower()
    if play_again not in ['y', 'yes', 'ok']:
        print("Thanks for playing! Goodbye.")
        break
