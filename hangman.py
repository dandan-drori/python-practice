import requests
import random
import math
import re

def get_random_word(size):
  word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
  response = requests.get(word_site)
  words = response.content.splitlines()
  word = random.choice(words)
  while len(word) < 5:
    word = random.choice(words)
  return word

def get_underscores(word, guessed_letters):
  underscores = ''
  for letter in word:
    if (letter in guessed_letters):
      underscores += letter + ' '
    else:
      underscores += '_ '
  return underscores

def draw_hangman(word, guessed_letters):
  stages_max_idx = 7
  wrong_guesses = 0
  for letter in guessed_letters:
    if letter not in word:
      wrong_guesses += 1
  print('Remaining Mistakes: ' + str(stages_max_idx - wrong_guesses))
  print(display_hangman(stages_max_idx - wrong_guesses))
  if wrong_guesses >= stages_max_idx:
    return 'LOSE'

def get_letter(word, guessed_letters):
  is_letter_valid = False
  while not is_letter_valid:
    letter = input('Please guess a letter: ').lower()
    regex = re.compile('[a-zA-Z]', re.IGNORECASE)
    if not regex.match(letter):
      print('Only latin letters allowed!')
      continue
    elif len(letter) > 1 or letter == '':
      print('Only one letter please...')
      continue
    elif letter in guessed_letters:
      print('You\'ve already guessed this letter!')
      continue
    else:
      is_letter_valid = True
    guessed_letters.append(letter)
    is_lose = draw_hangman(word, guessed_letters)
    if is_lose:
      return False
    print(get_underscores(word, guessed_letters))
  return letter

def is_game_over(letter, word, guessed_letters):
  if not letter:
    print('Game Over - You Lose')
    return True
  underscores = get_underscores(word, guessed_letters)
  if '_' not in underscores:
    print('You Won!')
    return True

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # hook
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]
  
def main():
  game_over = False
  word = str(get_random_word(10000))[2:-1]
  guessed_letters = []
  print('I thought of a word:')
  print(get_underscores(word, guessed_letters))
  while not game_over:
    letter = get_letter(word, guessed_letters)
    done = is_game_over(letter, word, guessed_letters)
    if done:
      print('The word was: ' + word)
      while input("Play Again? (Y/N) ").upper() == "Y":
        main()
      game_over = True
  
main()
