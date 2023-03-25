PIECE_INDICATORS = {
    "pawn_white": "P",
    "knight_white": "N",
    "bishop_white": "B",
    "rook_white": "R",
    "queen_white": "Q",
    "king_white": "K",
    "pawn_black": "p",
    "knight_black": "n",
    "bishop_black": "b",
    "rook_black": "r",
    "queen_black": "q",
    "king_black": "k",
}

PIECE_SCORES = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9,
    'king': 100
}

PIECE_MOVE_DELTA = {
    "pawn_white": [(-1, 0)],
    "knight_white": [(-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)],
    "bishop_white": [(-1, 1), (1, 1), (-1, -1), (1, -1), (-2, 2), (2, 2), (-2, -2), (2, -2), (-3, 3), (3, 3), (-3, -3), (3, -3), (-4, 4), (4, 4), (-4, -4), (4, -4), (-5, 5), (5, 5), (-5, -5), (5, -5), (-6, 6), (6, 6), (-6, -6), (6, -6), (-7, 7), (7, 7), (-7, -7), (7, -7)],
    "rook_white": [
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
        (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)
    ],
    "queen_white": [(-1, 1), (1, 1), (-1, -1), (1, -1), (-2, 2), (2, 2), (-2, -2), (2, -2), (-3, 3), (3, 3), (-3, -3), (3, -3), (-4, 4), (4, 4), (-4, -4), (4, -4), (-5, 5), (5, 5), (-5, -5), (5, -5), (-6, 6), (6, 6), (-6, -6), (6, -6), (-7, 7), (7, 7), (-7, -7), (7, -7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
    (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)],
    "king_white": [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)],
    "pawn_black": [(1, 0)],
}

PIECE_MOVE_DELTA["knight_black"] = PIECE_MOVE_DELTA["knight_white"]
PIECE_MOVE_DELTA["bishop_black"] = PIECE_MOVE_DELTA["bishop_white"]
PIECE_MOVE_DELTA["rook_black"] = PIECE_MOVE_DELTA["rook_white"]
PIECE_MOVE_DELTA["queen_black"] = PIECE_MOVE_DELTA["queen_white"]
PIECE_MOVE_DELTA["king_black"] = PIECE_MOVE_DELTA["king_white"]

LETTERS = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

class ChessBoard:
    def __init__(self, board=None):
        if board: self.board = board
        else: self.board = self.gen_board()

    def gen_board(self):
        board = []
        for _ in range(8):
            board.append([0] * 8)
        board[1] = ["pawn_black"] * 8
        board[6] = ["pawn_white"] * 8
        board[0] = ["rook_black", "knight_black", "bishop_black", "queen_black", "king_black", "bishop_black", "knight_black", "rook_black"]
        board[7] = ["rook_white", "knight_white", "bishop_white", "queen_white", "king_white", "bishop_white", "knight_white", "rook_white"]
        return board

    def print_board(self):
        for i, row in enumerate(self.board):
            print(f"{8-i} |", end="")
            for col in row:
                print(PIECE_INDICATORS[col] if col else " ", end="|")
            print(f" {i}")
            # print()
        print("   a|b|c|d|e|f|g|h")
        print("   0|1|2|3|4|5|6|7")

    def convert_pos_string_to_coords(self, pos_string):
        row, col =  8 - int(pos_string[1]), LETTERS[pos_string[0]]
        return row, col

    def convert_coords_to_pos_string(self, row, col):
        return f"{list(LETTERS.keys())[col]}{8-row}"

    def piece_at(self, row, col):
        return self.board[row][col]
    
    def get_pawn_moves(self, row, col, color):
        moves = []
        if color == "white":
            if row == 6:
                if self.board[row-1][col] == 0 and self.board[row-2][col] == 0:
                    moves.append((row-2, col))
            if self.board[row-1][col] == 0:
                moves.append((row-1, col))
            if col != 0 and self.board[row-1][col-1] != 0 and self.board[row-1][col-1].split()[1] == "black":
                moves.append((row-1, col-1))
            if col != 7 and self.board[row-1][col+1] != 0 and self.board[row-1][col+1].split()[1] == "black":
                moves.append((row-1, col+1))
        else:
            if row == 1:
                if self.board[row+1][col] == 0 and self.board[row+2][col] == 0:
                    moves.append((row+2, col))
            if self.board[row+1][col] == 0:
                moves.append((row+1, col))
            if col != 0 and self.board[row+1][col-1] != 0 and self.board[row+1][col-1].split()[1] == "white":
                moves.append((row+1, col-1))
            if col != 7 and self.board[row+1][col+1] != 0 and self.board[row+1][col+1].split()[1] == "white":
                moves.append((row+1, col+1))
        return moves
    
    def get_knight_moves(self, row, col, color):
        moves = []
        for row_delta, col_delta in PIECE_MOVE_DELTA["knight_" + color]:
            moves.append((row + row_delta, col + col_delta))
        return moves

    def get_move(self, pos_string):
        row, col =  self.convert_pos_string_to_coords(pos_string)
        if self.board[row][col] == 0: return []
        # print(row, col)
        piece, color = self.board[row][col].split("_")
        # print(f"row: {row}, col: {col}")
        moves = []
        if piece == "pawn":
            moves = self.get_pawn_moves(row, col, color)
        if piece == "knight":
            moves = self.get_knight_moves(row, col, color)
        # print(moves)
        n_moves = []
        for row, col in moves:
            if row < 0 or row > 7 or col < 0 or col > 7:
                continue
            n_moves.append((row, col))
        moves = n_moves
        n_moves = []
        # print(moves)
        for row, col in moves:
            if self.piece_at(row, col) != 0 and self.piece_at(row, col).split("_")[1] == color:
                continue
            n_moves.append((row, col))
        moves = n_moves
        mv_strings = [self.convert_coords_to_pos_string(row, col) for row, col in moves]
        return mv_strings
