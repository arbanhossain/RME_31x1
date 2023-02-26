from TicTacToe import Game, AI

player_num = int(input('Enter 1 for AI, 2 for Multiplayer: '))

game = Game()

if player_num == 1:
  ai = AI(game)
  print('AI is X')
game.print_board()
while True:
  if player_num == 1 and game.current_player == 'X':
    score, move = ai.value(game.board, 'X')
    print(move)
    row, col = move
  else:
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))
  game.make_move(row, col)
  game.print_board()
  if game.is_game_over(game.board):
    print('Game over!')
    winner = game.check_winner(game.board)
    if winner is None:
      print('It is a tie!')
    else:
      print(winner, 'wins!')
    break