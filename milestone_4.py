#!/bin/python3

import random

# genrate list of word for testing
word_list = ['Apple', 'Bannana', 'Peach', 'Pear', 'Rasberries']

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word) 
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.worssssd_list = word_list
        self.num_lives = num_lives

        def ask_for_input():
	
            while True:
                # Get user input
                guess = input('Please enter a single letter ',)

                if not len(guess)  == 1 and not guess.isalpha():
                    print('Invalid letter. Please, enter a single alphabetical character.')  
                elif guess in self.list_of_guesses:
                    print('You already tried that letter')
                else:
                    check_guess(self.word, guess = guess)
                    self.list_of_guesses.append(guess)

        def check_guess(word, guess):
            # Convert guess varaible to lower case
            guess = guess.lower()

            # Check using if stament if the chosen letter is in the word
            if guess in word:
                print("Good guess! {} is in the word.".format(guess))
                for letter in range(0, word):
                    if word[letter] == guess:
                        self.word_guessed[letter] = guess
                self.num_letters -= 1
            
            else:
                self.num_lives -= 1
                print("Sorry {} is not in the word.".format(guess))
                print("You have {} lives left".format(self.num_lives))
    
""" o = Hangman(word_list=word_list)
print(o.num_letters) """