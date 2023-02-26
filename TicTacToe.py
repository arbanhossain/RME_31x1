import random

class Game:
  def __init__(self):
    self.board = [['-','-','-'],
                  ['-','-','-'],
                  ['-','-','-']]
    # randomly select current player
    self.current_player = 'X' if random.randint(0,1) == 0 else 'O'
    self.winner = None
    self.game_over = False
  
  def switch_player(self):
    if self.current_player == 'X':
      self.current_player = 'O'
    else:
      self.current_player = 'X'
  
  def make_move(self, row, col):
    if self.board[row][col] == '-':
      self.board[row][col] = self.current_player
      self.switch_player()
    else:
      print('Invalid move!')
  
  def is_game_over(self, board):
    # check if there is no move to be made
    if self.check_winner(board) is not None:
      return True
    for row in board:
      for col in row:
        if col == '-':
          return False
    return True

  def check_winner(self, board):
    # check if there is a winner
    # check rows
    for row in board:
      if row[0] == row[1] == row[2] and row[0] != '-':
        return row[0]
    # check columns
    for col in range(len(board[0])):
      if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
        return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
      return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
      return board[0][2]
    return None
  
  def print_board(self):
    for row in self.board:
      for col in row:
        print(col, end=' ')
      print()

class AI:
  def __init__(self, game):
    self.game = game

  def get_available_moves(self):
    board = self.game.board
    moves = []
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == '-':
          moves.append((i,j))
    return moves
  
  def value(self, board, player):
    best_move = None
    if self.game.is_game_over(board):
      winner = self.game.check_winner(board)
      if winner == 'X':
        return [1, best_move]
      elif winner == 'O':
        return [-1, best_move]
      else:
        return [0, best_move]
    
    if player == 'X':
      best_score = -float('inf')
      for move in self.get_available_moves():
        board[move[0]][move[1]] = 'X'
        score, _ = self.value(board, 'O')
        board[move[0]][move[1]] = '-'
        if score > best_score:
          best_score = score
          best_move = move
      return [best_score, best_move]
    else:
      best_score = float('inf')
      for move in self.get_available_moves():
        board[move[0]][move[1]] = 'O'
        score, _ = self.value(board, 'X')
        board[move[0]][move[1]] = '-'
        if score < best_score:
          best_score = score
          best_move = move
      return [best_score, best_move]