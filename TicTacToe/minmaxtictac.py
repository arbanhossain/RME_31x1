from TicTacToe import Game, AI
import random

player_num = int(input('Enter 1 for AI, 2 for Multiplayer, 3 for two AIs: '))
rand_percent = 50
game = Game()
if player_num == 1:
  ai = AI(game)
  print('AI is X')
if player_num == 3:
  ai1 = AI(game)
  ai2 = AI(game)
game.print_board()
while True:
  if player_num == 3:
    if game.current_player == 'X':
      if random.randint(0, 100) <= rand_percent:
        move = ai1.get_available_moves()
        row, col = move[random.randint(0,len(move)-1)]
      else:
        score, move, ghurse = ai1.value(game.board, 'X', -float('inf'), float('inf'))
        row, col = move
      # print(ghurse)
    else:
      # score, move, ghurse = ai2.value(game.board, 'O', -float('inf'), float('inf'))
      if random.randint(0, 100) <= rand_percent:
        move = ai2.get_available_moves()
        row, col = move[random.randint(0,len(move)-1)]
      else:
        score, move, ghurse = ai1.value(game.board, 'O', -float('inf'), float('inf'))
        row, col = move
      # print(ghurse)
  elif player_num == 1 and game.current_player == 'X':
    score, move, ghurse = ai.value(game.board, 'X', -float('inf'), float('inf'))
    print(ghurse)
    row, col = move
  else:
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))
  game.make_move(row, col)
  game.print_board()
  print()
  if game.is_game_over(game.board):
    print('Game over!')
    winner = game.check_winner(game.board)
    if winner is None:
      print('It is a tie!')
    else:
      print(winner, 'wins!')
    break