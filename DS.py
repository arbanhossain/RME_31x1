import math

# Nodes for data structures that need a reference to the next item

class Node:

  def __init__(self, elem):
    self.value = elem
    self.next = None

# Stack Implementation (Using builtin python lists which work like arrays)

class Stack:
  
  def __init__(self, elem=None):
    if elem == None: self.arr = []
    elif isinstance(elem, list): self.arr = elem
    else: self.arr = [elem]

  def __str__(self):
    string = ""
    for i in reversed(self.arr):
      string += f"{str(i)}\n"
    return string

  # O(1)
  def is_empty(self):
    return len(self.arr) == 0
  
  # O(1)
  def push(self, elem):
    self.arr.append(elem)

  # O(1)
  def pop(self):
    return self.arr.pop()

  def display(self):
    for i in reversed(self.arr):
      print(i)

# Queue Implementation using a linked list

class Queue:

  def __init__(self):
    self.head = None
    self.tail = None
  
  def __str__(self):
    string = ""
    node = self.head
    while node != None:
      string += f"{str(node.value)}\n"
      node = node.next
    return string


  # O(1)
  def is_empty(self):
    return self.head == None
  
  # O(1)
  def enqueue(self, elem):
    node = Node(elem)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
  
  # O(1)
  def dequeue(self):
    if self.head == None: return None
    else:
      node = self.head
      self.head = self.head.next
      return node.value

# MaxHeap/Max-PriorityQueue implemented using arrays

class MaxHeap:

  def __init__(self):
    self.arr = []
    self.end = -1
  
  # Height, H = log(N)
  def get_height(self):
    return math.floor(math.log2(self.end + 1))

  def __str__(self):
    string = ""
    height = self.get_height()
    max_elems = 2 ** height

    for i in range(height + 1):
      elems = 2 ** i
      space = max_elems // elems
      for j in range(elems):
        if 2 ** i - 1 + j > self.end: break
        string += " " * space + str(self.arr[2 ** i - 1 + j]) + " " * space
      string += "\n"
    return string

  # O(H)
  def reheap_up(self, index):
    if index == 0: return
    parent = (index - 1) // 2
    if self.arr[index] > self.arr[parent]:
      self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
      self.reheap_up(parent)
  
  # O(H)
  def reheap_down(self, index):
    left = 2 * index + 1
    right = 2 * index + 2
    if left > self.end: return
    elif right > self.end:
      if self.arr[index] < self.arr[left]:
        self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
        self.reheap_down(left)
    else:
      if self.arr[left] > self.arr[right]:
        if self.arr[index] < self.arr[left]:
          self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
          self.reheap_down(left)
      else:
        if self.arr[index] < self.arr[right]:
          self.arr[index], self.arr[right] = self.arr[right], self.arr[index]
          self.reheap_down(right)
  
  # O(H)
  def enqueue(self, elem):
    self.arr.append(elem)
    self.end += 1
    self.reheap_up(self.end)
  
  # O(H)
  def dequeue(self):
    if self.end == -1: return None
    else:
      self.arr[0], self.arr[self.end] = self.arr[self.end], self.arr[0]
      self.end -= 1
      popped = self.arr.pop()
      self.reheap_down(0)
      return popped

# MinHeap/Min-PriorityQueue implemented using arrays

class MinHeap:
  
    def __init__(self):
      self.arr = []
      self.end = -1
    
    # Height, H = log(N)
    def get_height(self):
      return math.floor(math.log2(self.end + 1))
  
    def is_empty(self):
      return len(self.arr) == 0
    
    def __str__(self):
      string = ""
      height = self.get_height()
      max_elems = 2 ** height
  
      for i in range(height + 1):
        elems = 2 ** i
        space = max_elems // elems
        for j in range(elems):
          if 2 ** i - 1 + j > self.end: break
          string += " " * space + str(self.arr[2 ** i - 1 + j]) + " " * space
        string += "\n"
      return string

    # O(H)
    def reheap_up(self, index):
      if index == 0: return
      parent = (index - 1) // 2
      if self.arr[index] < self.arr[parent]:
        self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
        self.reheap_up(parent)
    
    # O(H)
    def reheap_down(self, index):
      left = 2 * index + 1
      right = 2 * index + 2
      if left > self.end: return
      elif right > self.end:
        if self.arr[index] > self.arr[left]:
          self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
          self.reheap_down(left)
      else:
        if self.arr[left] < self.arr[right]:
          if self.arr[index] > self.arr[left]:
            self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
            self.reheap_down(left)
        else:
          if self.arr[index] > self.arr[right]:
            self.arr[index], self.arr[right] = self.arr[right], self.arr[index]
            self.reheap_down(right)
    
    # O(H)
    def enqueue(self, elem):
      self.arr.append(elem)
      self.end += 1
      self.reheap_up(self.end)
    
    # O(H)
    def dequeue(self):
      if self.end == -1: return None
      else:
        self.arr[0], self.arr[self.end] = self.arr[self.end], self.arr[0]
        self.end -= 1
        popped = self.arr.pop()
        self.reheap_down(0)
        return popped

class Vertex:

  def __init__(self, name, value=None):
    self.value = value
    self.name = name

  def __hash__(self):
    return hash(f"{self.value}+{self.name}")
  
  def __eq__(self, other):
    return self.value == other.value
  
  def __ne__(self, other):
    return not(self == other)
  
  def __str__(self):
    return str(self.value)

# Space: O(V) for vertices and O(E) for adjacency list. O(V+E)
class Graph:

  def __init__(self):
    self.adjacency_list = {}
    self.vertices = {}
    self.weights = {}
  
  def add_undirected_edge(self, v1, v2, weight=1):
    # add vertex in vertices if not already there
    if v1.name not in self.vertices:
      self.vertices[v1.name] = v1
    if v2.name not in self.vertices:
      self.vertices[v2.name] = v2
    
    # add v2 in v1's adjacency list
    if v1.name in self.adjacency_list:
      self.adjacency_list[v1.name].append(v2.name)
    else:
      self.adjacency_list[v1.name] = [v2.name]
    
    # add v1 in v2's adjacency list
    if v2.name in self.adjacency_list:
      self.adjacency_list[v2.name].append(v1.name)
    else:
      self.adjacency_list[v2.name] = [v1.name]
    
    # add weight in weights
    if v1.name in self.weights:
      self.weights[v1.name][v2.name] = weight
    else:
      self.weights[v1.name] = {v2.name: weight}
    
    if v2.name in self.weights:
      self.weights[v2.name][v1.name] = weight
    else:
      self.weights[v2.name] = {v1.name: weight}
  
  def add_directed_edge(self, v1, v2, weight=1):
    # add vertex in vertices if not already there
    if v1.name not in self.vertices:
      self.vertices[v1.name] = v1
    if v2.name not in self.vertices:
      self.vertices[v2.name] = v2
    
    # add v2 in v1's adjacency list
    if v1.name in self.adjacency_list:
      self.adjacency_list[v1.name].append(v2.name)
    else:
      self.adjacency_list[v1.name] = [v2.name]
    
    if v2.name not in self.adjacency_list:
      self.adjacency_list[v2.name] = []
    
    # add weight in weights
    if v1.name in self.weights:
      self.weights[v1.name][v2.name] = weight
    else:
      self.weights[v1.name] = {v2.name: weight}
  
  # this traverse will take some time more than O(V+E) as we are also building the traverse_order list [+ O(V.2E)].
  def bfs_traverse(self, source):
    traverse_order = []
    visited = set()
    queue = Queue()
    queue.enqueue(source)

    appended = set()
    traverse_order.append([source])
    appended.add(source)

    while not queue.is_empty():
      level = []
      current = queue.dequeue()
      if current not in visited:
        visited.add(current)
        for neighbor in self.adjacency_list[current]:
          
          if neighbor not in appended:
            appended.add(neighbor)
            level.append(neighbor)
          
          queue.enqueue(neighbor)
        if level != []: traverse_order.append(level)
    return traverse_order
  
  # O(V+E)
  # reverse the return value of this method to get the topological sort of the graph
  def dfs_traverse(self, source):
    traverse_order = []
    visited = set()
    stack = Stack()
    stack.push(source)
    while not stack.is_empty():
      current = stack.pop()
      if current not in visited:
        traverse_order.append(current)
        visited.add(current)
        for neighbor in self.adjacency_list[current]:
          stack.push(neighbor)
    return traverse_order
  
  def path_exists_bfs(self, v1, v2):
    queue = Queue()
    queue.enqueue(v1)
    visited = set()
    while not queue.is_empty():
      current = queue.dequeue()
      if current not in visited:
        visited.add(current)
        if current == v2:
          return True
        for neighbor in self.adjacency_list[current]:
          if neighbor == v2:
            return True
          queue.enqueue(neighbor)
    return False