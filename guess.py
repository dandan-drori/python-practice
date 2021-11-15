import math
import random
import re

def check_game_over(guess, num):
  if (guess == num):
    print('Correct!')
    again = input('Play Again? ')
    regex = re.compile('ye(s|ah|p)', re.IGNORECASE)
    if (regex.match(again)):
      main()
    else:
      print('Too bad :(\nSee you later...')

def check_guess(relative, guess, num):
  print('The number you chose was too {}!'.format(relative))
  return int(input('Your Guess? '))
  

def main():
  num = math.floor(random.random()*100)
  guess = int(input('I thought of a number between 0 - 100, try to guess it.\nYour Guess? '))
  while not guess == num:
    comparison = ''
    if (guess > num):
      comparison = 'high'
    elif (guess < num):
      comparison = 'low'
    guess = check_guess(comparison, guess, num)
    check_game_over(guess, num)

main()

''' 

Instructions and Guidelines for Guess.py 

General Overview: 

while loop 

generate a random number within bounds using:

  - import random
  - random.random()

  - import math
  - math.floor()

  take input from player

  compare input to generated number and 
  give feedback to the player

  the game continues untill the player guesses the generated number

Pay Attention to:

  Try to use more than one function other than "main"

  Variable Types: 
    - An input from the player is always a string. If you need to use it as a number, first convert it to one.
    - If you want to print a number with a string, don't forget to first convert the number to a string.

  Your code should not exceed 60 lines. 

Starting Code:

import random
import math

# random.random() - generates a random number (float) between 0 and 1
# math.floor(yourNumber) - rounds the given 'yourNumber' downwards, i.e. removes the numbers after the floating point

def main():
  # Your code starts here
  pass # Remove this line

main()

'''
