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