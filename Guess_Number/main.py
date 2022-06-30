import random

# generate a random number then
# the user will then have to guess the randomly generated number
# input: integer representing the upper bound of numerical possiblities
# output: a string congratulating the user for winning

def guess(x):
    random_number = random.randint(1, x)
    attempt = 0
    while attempt != random_number:
        attempt = int(input(f"Guess a number between 1 and {x}: "))
        if attempt < random_number:
            print  ("Too Small! Guess again.")
        elif attempt > random_number:
            print ("Too Big! Guess again.")
    return f"You guessed the number {random_number} correctly!"

#print (guess(100))

# the user will think of a random number and the computer will play a guessing game to guess that number

# input: integer that defines the upper bound of random number generation
# output: a string congratulating the program for winning the game
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        # this if/else block account for the case 
        # when low and high are equal, which would break randint()
        if  low != high:
            guess = random.randint(low, high)
        else:
            # we still need a guess, however, to have the program take one final, correct guess.
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            # minus 1 since randint has inclusive bounds
            high = guess-1
        elif feedback == 'l':
            # plus 1 since randint has inclusive bounds            
            low = guess + 1
    return f"Yay! The computer guessed your number, {guess}, correctly!"

print (computer_guess(100))