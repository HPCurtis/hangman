#!/bin/python3

# Import  python modules used within script
import random


def hangman():
	word = word_gen()
	guess = ask_for_input()
	check_guess(word, guess)

def word_gen():
	word_list = ['Apple', 'Bannana', 'Peach', 'Pear', 'Rasberries']
	word = random.choice(word_list)
	return(word)

def ask_for_input():
	
	while 0 == 0:
		# Get user input
		guess = input('Please enter a single letter ',)

		if len(guess) == 1 and guess.isalpha():
			print('Good guess')
			break
		else:
			print('Invalid letter. Please, enter a single alphabetical character.')
	return(guess)

def check_guess(word, guess):

	# COnvert guess varaible to lower case
	guess = guess.lower()
	if guess in word:
		print("Good guess! {} is in the word.".format(guess))
	else:
		print("Sorry {} is not in the word. Try again.".format(guess))

hangman()
