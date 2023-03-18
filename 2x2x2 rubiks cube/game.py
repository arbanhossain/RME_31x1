# needs more optimization

import sys

sys.path.append('..')
from DS import Queue

class Node:

    def __init__(self, elem, move_name=None, parent=None):
        self.value = elem
        self.next = None
        self.parent = parent
        self.move_name = move_name

class ModQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if self.head == None: return None
        else:
            node = self.head
            self.head = self.head.next
            return node

global front, top, left, right, back, bottom

front = ["white", "white", "white", "white"]
top = ["green", "green", "green", "green"]
left = ["red", "red", "red", "red"]
right = ["orange", "orange", "orange", "orange"]
back = ["yellow", "yellow", "yellow", "yellow"]
bottom = ["blue", "blue", "blue", "blue"]

def move_R():
    front[1], front[3], top[1], top[3], back[0], back[2], bottom[1], bottom[3] = bottom[1], bottom[3], front[1], front[3], top[3], top[1], back[2], back[0]
    global right
    right = [
        right[2],
        right[0],
        right[3],
        right[1],
    ]

def move_F():
    top[2], top[3], left[1], left[3], bottom[0], bottom[1], right[0], right[2] = left[3], left[1], bottom[0], bottom[1], right[2], right[0], top[2], top[3]
    global front
    front = [
        front[2],
        front[0],
        front[3],
        front[1],
    ]

def move_U():
    front[0], front[1], left[0], left[1], back[0], back[1], right[0], right[1] = right[0], right[1], front[0], front[1], left[0], left[1], back[0], back[1]
    global top
    top = [
        top[2],
        top[0],
        top[3],
        top[1],
    ]

def move_L():
    top[0], top[2], front[0], front[2], bottom[0], bottom[2], back[1], back[3] = back[3], back[1], top[0], top[2], front[0], front[2], bottom[2], bottom[0]
    global left
    left = [
        left[2],
        left[0],
        left[3],
        left[1],
    ]

def move_B():
    top[0], top[1], right[1], right[3], bottom[2], bottom[3], left[0], left[2] = right[1], right[3], bottom[3], bottom[2], left[0], left[2], top[1], top[0]
    global back
    back = [
        back[2],
        back[0],
        back[3],
        back[1],
    ]

def move_D():
    front[2], front[3], right[2], right[3], back[2], back[3], left[2], left[3] = left[2], left[3], front[2], front[3], right[2], right[3], back[2], back[3]
    global bottom
    bottom = [
        bottom[2],
        bottom[0],
        bottom[3],
        bottom[1],
    ]

def move_R2():
    move_R()
    move_R()

def move_F2():
    move_F()
    move_F()

def move_U2():
    move_U()
    move_U()


# inverse of the moves
def move_Ri():
    for _ in range(3):
        move_R()

def move_Fi():
    for _ in range(3):
        move_F()

def move_Li():
    for _ in range(3):
        move_L()

def move_Bi():
    for _ in range(3):
        move_B()

def move_Ui():
    for _ in range(3):
        move_U()

def move_Di():
    for _ in range(3):
        move_D()


moves = [
    {"move": move_R, "inverse_move": move_Ri, "move_name": "R"},
    {"move": move_F, "inverse_move": move_Fi, "move_name": "F"},
    {"move": move_U, "inverse_move": move_Ui, "move_name": "U"},
    {"move": move_Ri, "inverse_move": move_R, "move_name": "R\'"},
    {"move": move_Fi, "inverse_move": move_F, "move_name": "F\'"},
    {"move": move_Ui, "inverse_move": move_U, "move_name": "U\'"},
    {"move": move_R2, "inverse_move": move_R2, "move_name": "R2"},
    {"move": move_F2, "inverse_move": move_F2, "move_name": "F2"},
    {"move": move_U2, "inverse_move": move_U2, "move_name": "U2"},

]

def print_cube():
    print(f"front {front}")
    print(f"top {top}")
    print(f"left {left}")
    print(f"right {right}")
    print(f"back {back}")
    print(f"bottom {bottom}")

def is_cube_solved():
    return len(set(front)) == len(set(top)) == len(set(left)) == len(set(right)) == len(set(back)) == len(set(bottom)) == 1

def is_anti_move(move1: str, move2: str):
    if move1 == move2:
        if len(move1) == len(move2) == 2 and move1[1] == '2':
            return True
        return False
    if move1 == move2 + "'":
        return True
    if move1 + "'" == move2:
        return True
    return False

# print_cube()
# scramble = "R F F R R U U F R R F U U R'".split()
scramble = "F' R U2 R2 F' U' R".split()
# scramble = []
for move in scramble:
    if move == 'R': move_R()
    elif move == 'R\'': move_Ri()
    elif move == 'F': move_F()
    elif move == 'F\'': move_Fi()
    elif move == 'U': move_U()
    elif move == 'U\'': move_Ui()
    elif move == 'R2': move_R2()
    elif move == 'F2': move_F2()
    elif move == 'U2': move_U2()
print_cube()
visited = []
q = ModQueue()

cube = [front, top, left, right, back, bottom]

q.enqueue(Node(cube))

e = 0

soln = None
solved = False
while not q.is_empty():
    if len(visited)%1000 == 0: print(len(visited))
    cube = q.dequeue()
    front, top, left, right, back, bottom = cube.value
    # print("CUBE")
    # print(cube.move_name)
    # print_cube()
    if is_cube_solved():
        print("ALREADY SOLVED")
        exit()
    if sorted(cube.value) not in visited:
        # e+=1
        visited.append(sorted(cube.value))
        # print("children")
        # print("-"*30)
        for move in moves:
            if cube.move_name and is_anti_move(cube.move_name, move["move_name"]): continue
            move["move"]()
            # print(move["move_name"])
            # print_cube()
            # print()
            if is_cube_solved():
                soln = Node([list(front), list(top), list(left), list(right), list(back), list(bottom)], move_name=move["move_name"], parent=cube)
                solved = True
                break
            q.enqueue(Node([list(front), list(top), list(left), list(right), list(back), list(bottom)], move_name=move["move_name"], parent=cube))
            move["inverse_move"]()
    if solved:
        break
    # input()

sols = []

if soln is not None:
    print("SOLUTION")
    while soln is not None:
        if soln.move_name:
            sols.append(soln.move_name)
            print(soln.move_name)
        print(soln.value)
        soln = soln.parent

print(" ".join(sols[::-1]))