import random

# define the game rules
rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

# define the options for the player
options = ['rock', 'paper', 'scissors']

# initialize the player's score
score = 0

# main game loop
while True:
    # ask the player for their choice
    player_choice = input('Choose rock, paper, or scissors: ').lower()

    # validate the player's choice
    if player_choice not in options:
        print('Invalid choice, try again.')
        continue

    # let the computer choose a random option
    computer_choice = random.choice(options)

    # print the choices
    print(f'You chose {player_choice}, computer chose {computer_choice}.')

    # determine the winner
    if player_choice == computer_choice:
        print('Tie!')
    elif rules[player_choice] == computer_choice:
        print('You win!')
        score += 1
    else:
        print('You lose!')

    # ask the player if they want to play again
    play_again = input('Do you want to play again? (y/n)').lower()
    if play_again != 'y':
        break

# print the final score
print(f'Your score is {score}.')