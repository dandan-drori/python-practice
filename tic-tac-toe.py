import random
import re

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
        b[i][j] = cell.replace("'", "")
      else:
        b[i][j] = int(board[i][j])
  print('- - - - - - - - - -')
  print(str(b[0]) + '\n' + str(b[1]) + '\n' + str(b[2]))
  print('- - - - - - - - - -')

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
  print_board(board)
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
      print(get_other_player(turn) + ' has won!')
      while input('Play Again? Y/N ').upper() == 'Y':
        main()
      game_over = True

main()
