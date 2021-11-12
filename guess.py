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
    if (guess > num):
      guess = check_guess('high', guess, num)
      check_game_over(guess, num)
    elif (guess < num):
      guess = check_guess('low', guess, num)
      check_game_over(guess, num)

main()
