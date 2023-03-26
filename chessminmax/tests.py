from utils import *

b = ChessBoard()
b.print_board()

# while True:
#     mvs = b.get_move(input("Enter pos: "))
#     print(mvs)
#     for mv in mvs:
#         # print(mv)
#         print(b.convert_coo

assert set(b.get_move("a2")) == set(["a3", "a4"])
assert set(b.get_move("a7")) == set(["a6", "a5"])
assert set(b.get_move("b2")) == set(["b3", "b4"])
assert set(b.get_move("b7")) == set(["b6", "b5"])
assert set(b.get_move("c2")) == set(["c3", "c4"])
assert set(b.get_move("c7")) == set(["c6", "c5"])
assert set(b.get_move("d2")) == set(["d3", "d4"])
assert set(b.get_move("d7")) == set(["d6", "d5"])
assert set(b.get_move("e2")) == set(["e3", "e4"])
assert set(b.get_move("e7")) == set(["e6", "e5"])
assert set(b.get_move("f2")) == set(["f3", "f4"])
assert set(b.get_move("f7")) == set(["f6", "f5"])
assert set(b.get_move("g2")) == set(["g3", "g4"])
assert set(b.get_move("g7")) == set(["g6", "g5"])
assert set(b.get_move("h2")) == set(["h3", "h4"])
assert set(b.get_move("h7")) == set(["h6", "h5"])

assert set(b.get_move("b1")) == set(["a3", "c3"])