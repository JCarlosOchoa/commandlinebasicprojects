import random

def play():
    # user inputs their choice
    # computer inputs their choice
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    # now we must decide who won or if there is a tie
    if user == computer:
        return "It's a tie!"

    elif is_win(user, computer):
        return "You win!"
    
    return "Computer wins!"


def is_win(player, opponent):
    # input player choices in r/p/s game
    # output true if player wins
    # r > s, s > p, p > r 
    if (player == 'r' and opponent == "s") or \
        (player == 's' and opponent == "p") or \
        (player == 'p' and opponent == "r"):
        return True

print (play())