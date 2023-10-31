#!/bin/python3

import random

# genrate list of word for testing
word_list = ['Apple', 'Bannana', 'Peach', 'Pear', 'Rasberries']

# Create hangman game class
class Hangman():

    def __init__(self, word_list, num_lives = 5):
        # Define class attributes
        self.word = str(random.choice(word_list)).lower()
        self.word_guessed = ['_'] * len(self.word) 
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.worssssd_list = word_list
        self.num_lives = num_lives

    # Geberate ask input method
    def ask_for_input(self):

        while True:
            # Get user input
            guess = input('Please enter a single letter ',)

            if not len(guess)  == 1 and not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')  

            elif guess in self.list_of_guesses:
                print('You already tried that letter')

            else:
                self.check_guess(self.word, guess = guess)
                self.list_of_guesses.append(guess)
                break
        
        return(guess)

    # Generate check_guess method.
    def check_guess(self, word, guess):
        # Convert guess varaible to lower case
        guess = guess.lower()

        # Check using if statement if the chosen letter is in the word
        if guess in word:
            print("Good guess! {} is in the word.".format(guess))

            for letter in range(0, len(word)):
                if word[letter] == guess:
                    self.word_guessed[letter] = guess

            # Subract one from number of letter to guess.        
            self.num_letters -= 1
        
        else:
            # Guess is wrong so remove one life.
            self.num_lives -= 1

            # Output messages to user.
            print("Sorry {} is not in the word.".format(guess))
            print("You have {} lives left".format(self.num_lives))



# Generate play game function
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)


    while True == True:
         if game.num_lives == 0:
             print('You lost')
             break
         
         elif game.num_letters > 0:
            game.ask_for_input()

         else:
             print('Congratulations. You won the game!')
             break
        
play_game(word_list)
     
            
