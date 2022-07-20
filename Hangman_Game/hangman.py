import random
from string import ascii_uppercase
from words import words

def hangman():
    word = random.choice(words).upper()
    word_letters = set(word) #letters in the word
    alphabet = set(ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    #get user input
    while len(word_letters) > 0 and lives > 0:

        print ("------------------------------------")

        # let the user know how many lives are left
        # let the user know what letters have been used before they make a guess
        print ("You have ", lives,  " lives left and you have used these letters: ", " ".join(used_letters))

        # let the user know what the current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]

        print ("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print ("Your letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character! Try a different one.")
        
        else:
            print("Invalid character.")
    
    if lives != 0:
        return f"You got it! You guessed the word {word}!"
    else: 
        return "You lost! The word was " + word

print (hangman())