#!/bin/python3

# Import  python modules used within script
import random

word_list = ['Apple', 'Bannana', 'Peach', 'Pear', 'Rasberries']
word = random.choice(word_list)

# Get user input
guess = input('Please enter a single letter ',)

# Check user input 

if len(guess) == 1 and guess.isalpha():
	print('Good guess') 
else:
	print('Oops! That is not a valid input')
