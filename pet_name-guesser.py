# Pet Name Guessing Game

# Imports
import argparse
import petname
import sys
import random

# Generates a random pet name
parser = argparse.ArgumentParser(description='Generate human readable random names')
parser.add_argument('-w', '--words', help='Number of words in name, default=1', default=1)
parser.options = parser.parse_args()

petName = petname.Generate(int(parser.options.words)) # Pet name generated

# Generates the blanked word
blank = petName
numBlanks = random.randint(1, len(petName)-2) # Randomly generated number of blanks

for i in range(0, numBlanks, 1):
    chk = True # Checks if the blanked word already has a "_" at the randomly generated index (True means the blanked word already has a "_", vice versa for False)
    while chk:
        blankInd = random.randint(0, len(petName)-1) # Generates random index to blank at
        if(blank[blankInd] == "_"):
            chk = True # Retry to get the blank index as it already has a "_"
        else:
            blank = blank[:blankInd] + "_" + blank[blankInd + 1:] # Replaces the character at the randomly generated index in blank with a "_" 
            chk = False

tries = numBlanks * 2 # Number of tries for the user
counter = 0 # The counter to keep the current try's number in check
    
# Instructions to the game
print("Guess the Pet Name. You have " + str(tries) + " tries.")
print("Type a letter in lowercase, then put a space, and after that input a number within the range of the blank word")
print("(where you think the letter is to be placed within the blanked word). (ie: d 2)")
print("NOTE: The first letter is on position number 1 in the blank word, the second letter is number 2...")