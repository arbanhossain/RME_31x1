from utils import *

custom_board = [
    ["rook_black", "knight_black", "bishop_black", "queen_black", "king_black", "bishop_black", "knight_black", "rook_black"],
    ["pawn_black", "pawn_black", "pawn_black", "pawn_black", "pawn_black", "pawn_black", "pawn_black", "pawn_black"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, "knight_white", 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["pawn_white", 0, 0, 0, "pawn_white", 0, 0, 0],
    [0, "pawn_white", "pawn_white", "pawn_white", 0, "pawn_white", "pawn_white", "pawn_white"],
    ["rook_white", 0, "bishop_white", "queen_white", "king_white", "bishop_white", "knight_white", "rook_white"]
]

b = ChessBoard(custom_board)
b.print_board()

while True:
    mvs = b.get_move(input("Enter pos: "))
    print(mvs)