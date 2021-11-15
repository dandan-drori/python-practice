import random
import re

score = {
  'X': 0,
  'O': 0,
}

class clrs:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' 

def get_empty_board():
  return [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
  ]

def print_board(board):
  b = get_empty_board()
  for i in range(3):
    for j in range(3):
      cell = board[i][j]
      if cell == 'X' or cell == 'O':
        b[i][j] = cell
      else:
        b[i][j] = int(board[i][j])
  for i in range(3):
    for j in range(3):
      if b[i][j] == 'X':
        if j == 2:
          print(clrs.WARNING + b[i][j] + clrs.ENDC, end='')
        else:
          print(clrs.WARNING + b[i][j] + clrs.ENDC + ' | ', end='')
      elif b[i][j] == 'O':
        if j == 2:
          print(clrs.FAIL + b[i][j] + clrs.ENDC, end='')
        else:
          print(clrs.FAIL + b[i][j] + clrs.ENDC + ' | ', end='')
      else:
        print(b[i][j], end='')
        if j < 2:
          print(' | ', end='')
    if i < 2:
      print('\n-   -   -')
    else:
      print('\n')

def is_game_over(board):
  regex = re.compile('[0-9]')
  # check rows
  for row in board:
    if row[0] == row[1] == row[2] and not regex.match(row[0]):
      return True
  
  # check columns
  if board[0][0] == board[1][0] == board[2][0] and not regex.match(board[0][0]):
    return True
  if board[0][1] == board[1][1] == board[2][1] and not regex.match(board[0][1]):
    return True
  if board[0][2] == board[1][2] == board[2][2] and not regex.match(board[0][2]):
    return True

  # check diagonals
  if board[0][0] == board[1][1] == board[2][2] and not regex.match(board[0][0]):
    return True
  if board[0][2] == board[1][1] == board[2][0] and not regex.match(board[1][1]):
    return True

def get_empty_cells(board):
  empty_cells = []
  regex = re.compile('[0-9]')
  for i in range(3):
    for j in range(3):
      cell = board[i][j]
      if regex.match(cell):
        empty_cells.append(cell)
  return empty_cells

def player_move(board):
  print_board(board)
  move = input('Your move? ')
  empty_cells = get_empty_cells(board)
  while not move in empty_cells:
    print_board(board)
    move = input('Invalid move, choose another: ')
  for i in range(3):
    for j in range(3):
      if board[i][j] == move:
        board[i][j] = 'X'
  return board
      
def computer_move(board):
  #print_board(board)
  empty_cells = get_empty_cells(board)
  if not len(empty_cells):
    return False
  move = random.choice(empty_cells)
  for i in range(3):
    for j in range(3):
      if board[i][j] == move:
        board[i][j] = 'O'
  return board

def get_other_player(turn):
  if turn == 'X':
    return 'O'
  elif turn == 'O':
    return 'X'
  else:
    return 'Draw'

def print_score():
  print('score - X : ', end='')
  print(score['X'], end='')
  print(' | ', end='')
  print('O : ', end='')
  print(score['O'])

def main():
  board = get_empty_board()
  game_over = False
  turn = 'X'
  while not game_over:
    if turn == 'X':
      board = player_move(board)
      turn = 'O'
    else:
      board = computer_move(board)
      turn = 'X'
    if not board:
      turn = 'Draw'
      done = True
    done = is_game_over(board)
    if done:
      print_board(board)
      winner = get_other_player(turn)
      print(winner + ' has won!')
      score[winner] += 1
      print_score()
      while input('Play Again? Y/N ').upper() == 'Y':
        main()
      game_over = True

main()
