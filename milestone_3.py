#!/bin/python3

# Import  python modules used within script
import random

# Create hangman function that like a main() function.
def hangman():
	'''
	
	'''
	word = word_gen()
	guess = ask_for_input()
	check_guess(word, guess)

# Create word generator function.
def word_gen():
	'''
	'''
	word_list = ['Apple', 'Bannana', 'Peach', 'Pear', 'Rasberries']
	word = random.choice(word_list)
	return(word)

# Generate function to get user input.
def ask_for_input():
	'''
	'''
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
	'''
	'''
	# Convert guess variable to lower case
	guess = guess.lower()

	# Check using if stament if the chosen letter is in the word
	if guess in word:
		print("Good guess! {} is in the word.".format(guess))
	else:
		print("Sorry {} is not in the word. Try again.".format(guess))

# Call the hangman function.
hangman()
