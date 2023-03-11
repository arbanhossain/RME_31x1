import sys
import hashlib
sys.path.append('..')
from DS import MinHeap

class State:
  def __init__(self, board, g, parent=None):
    self.board = board
    self.parent = parent
    self.g = g
    self.h = 0
    for i in range(len(board)):
      if board[i] != i+1:
        self.h += 1
  
  def get_children(self):
    state = self.board
    blank = state.index(0)

    bottom = blank + 3
    top = blank - 3

    left = blank - 1
    right = blank + 1

    children = []
    if bottom in range(0,9):
      arr = list(self.board)
      arr[blank], arr[bottom] = arr[bottom], arr[blank]
      children.append(arr)
    if top in range(0,9):
      arr = list(self.board)
      arr[blank], arr[top] = arr[top], arr[blank]
      children.append(arr)
    if right//3 == blank//3:
      arr = list(self.board)
      arr[blank], arr[right] = arr[right], arr[blank]
      children.append(arr)
    if left//3 == blank//3:
      arr = list(self.board)
      arr[blank], arr[left] = arr[left], arr[blank]
      children.append(arr)

    return children
  
  def __hash__(self):
    return int(hashlib.sha256(("".join([str(x) for x in self.board])).encode('utf-8')).hexdigest(), 16) % 10**8
  
  def __eq__(self, other):
    return self.board == other.board

class BoardNode:
  def __init__(self, state, priority):
    self.state = state
    self.priority = priority
  
  def __lt__(self, other):
    return self.priority < other.priority
  
  def __eq__(self, other):
    return self.state == other.state
  
  def __gt__(self, other):
    return self.priority > other.priority

def print_board(board):
  for i in range(9):
    if board[i] == 0: print(' ', end=" ")
    else: print(board[i], end=" ")
    if i % 3 == 2: print()

def shuffle(board):
  import random
  for _ in range(100):
    children = State(board, 0).get_children()
    board = random.choice(children)
  return board

GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# INITIAL = [1, 2, 3, 0, 4, 6, 7, 5, 8]
INITIAL = shuffle(list(GOAL))

q = MinHeap()

q.enqueue(BoardNode(State(INITIAL, 0), 0))
visited = {}

final_state = None

while not q.is_empty():
  current = q.dequeue().state

  if current.board == GOAL:
    print("Found solution!")
    final_state = current
    break
  
  children = current.get_children()
  for child in children:
    child_node = State(child, current.g + 1, current)
    if child_node not in visited:
      visited[child_node] = child_node
      q.enqueue(BoardNode(child_node, child_node.g + child_node.h))
    else:
      if visited[child_node].g > child_node.g:
        visited[child_node] = child_node

if final_state is None:
  print("No solution found")
  exit()

c = final_state

arr = []

while c is not None:
  arr.append(c.board)
  c = c.parent

arr.reverse()

for i in arr:
  print_board(i)
  print()