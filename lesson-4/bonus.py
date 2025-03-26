import random

player_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

print("Welcome to Rock, Paper, Scissors! First to 5 points wins.")

while player_score < 5 and computer_score < 5:
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in choices:
        print("Invalid choice, please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score - You: {player_score}, Computer: {computer_score}")

if player_score == 5:
    print("You won the game!")
else:
    print("Computer won the game!")
