import math

class Node:

  def __init__(self, elem):
    self.value = elem
    self.next = None

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

  def is_empty(self):
    return len(self.arr) == 0
  
  def push(self, elem):
    self.arr.append(elem)

  def pop(self):
    return self.arr.pop()

  def display(self):
    for i in reversed(self.arr):
      print(i)


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

  def is_empty(self):
    return self.head == None
  
  def enqueue(self, elem):
    node = Node(elem)
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
      return node.value

class MaxHeap:

  def __init__(self):
    self.arr = []
    self.end = -1
  
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

  def reheap_up(self, index):
    if index == 0: return
    parent = (index - 1) // 2
    if self.arr[index] > self.arr[parent]:
      self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
      self.reheap_up(parent)
  
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
  
  def enqueue(self, elem):
    self.arr.append(elem)
    self.end += 1
    self.reheap_up(self.end)
  
  def dequeue(self):
    if self.end == -1: return None
    else:
      self.arr[0], self.arr[self.end] = self.arr[self.end], self.arr[0]
      self.end -= 1
      popped = self.arr.pop()
      self.reheap_down(0)
      return popped

class MinHeap:
  
    def __init__(self):
      self.arr = []
      self.end = -1
    
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
  
    def reheap_up(self, index):
      if index == 0: return
      parent = (index - 1) // 2
      if self.arr[index] < self.arr[parent]:
        self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
        self.reheap_up(parent)
    
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
    
    def enqueue(self, elem):
      self.arr.append(elem)
      self.end += 1
      self.reheap_up(self.end)
    
    def dequeue(self):
      if self.end == -1: return None
      else:
        self.arr[0], self.arr[self.end] = self.arr[self.end], self.arr[0]
        self.end -= 1
        popped = self.arr.pop()
        self.reheap_down(0)
        return popped

class Vertex:

  def __init__(self, value=None):
    self.value = value

  def __hash__(self):
    return hash(self.value)
  
  def __eq__(self, other):
    return self.value == other.value
  
  def __ne__(self, other):
    return not(self == other)
  
  def __str__(self):
    return str(self.value)

class Graph:

  def __init__(self):
    self.adjacency_list = {}
  
  def add_undirected_edge(self, v1, v2):
    if v1 in self.adjacency_list:
      self.adjacency_list[v1].append(v2)
    else:
      self.adjacency_list[v1] = [v2]
    
    if v2 in self.adjacency_list:
      self.adjacency_list[v2].append(v1)
    else:
      self.adjacency_list[v2] = [v1]
  
  def add_directed_edge(self, v1, v2):
    if v1 in self.adjacency_list:
      self.adjacency_list[v1].append(v2)
    else:
      self.adjacency_list[v1] = [v2]
    
    if v2 not in self.adjacency_list:
      self.adjacency_list[v2] = []
  
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