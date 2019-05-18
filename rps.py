# rps.py

import random

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def random_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    elif human == 'scissors' and computer == 'paper':
        return 'human'
    elif human == 'scissors' and computer == 'rock':
        return 'computer'
    elif human == 'paper' and computer == 'scissors':
        return 'computer'
    elif human == 'paper' and computer == 'rock':
        return 'human'
    elif human == 'rock'and computer == 'paper':
        return 'computer'
    elif human == 'rock'and computer == 'scissors':
        return 'human'

def main(load=input):
    human = None
    while not is_valid_play(human):
        human = load('rock, paper or scissors? ')

    computer = random_play()
    print(computer)
    print(determine_game_result(human, computer))

if __name__ == '__main__':
    main()
