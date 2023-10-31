# Hangman

## Project description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The aim of the project is to show the progressive build and refactoring of a hangman game code into separate milestones as specified by the Aicore bootcamp project.

## Installatiioon instructions
To to run this the code user only needs base python to be intalled as no external dependencies are required outside those that are impotable from from base python. See, https://www.python.org/downloads/ to find instructions and download python if required.


# File structure

## ReadMe.md 
The file you're reading now.

## Milestone_2.py
Python script showing the creation of a word list variable with the use of random module to randomly select a word from this list. With this user input can then be acquired and then assesesed using conditonal statements. In this case the if and else statements.

# milestone_3.py 
This python script takes the priiciples from milestone_2.py but extends them by creating functions of all these principles in code to allow for their repeated use moving forward in the project. Specifcally the code was functionalised into check_guess and ask_for_input functions. 

## milestone_4.py
This python script is the encapuslation of the functions generated in milestone_3.py into the Hangman class follwing object orientated programming principles

## milestone_5.py
Finally this Python script is the creation of the hangamn game using the Hangman class and condtional statemetns to impy the game process with and instance of the Hangman class. 

## Usage instructions
As a game the hangman can be played by running the final milestone_5.py files as that has the game function called and the user simple has to follow the instructions on the terminal to give their chosen letter responses for the Hangman game.

## License 
   Copyright [2023] [Harrison Curtis]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.