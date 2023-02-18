import math

class PriorityNode:

  def __init__(self, value, priority):
    self.value = value
    self.priority = priority
  
  def __lt__(self, __o):
    return self.priority < __o.priority
  
  def __gt__(self, __o):
    return self.priority > __o.priority
  
  def __eq__(self, __o):
    return self.priority == __o.priority
  
  def __le__(self, __o):
    return self.priority <= __o.priority
  
  def __ge__(self, __o):
    return self.priority >= __o.priority
  
  def __str__(self):
    return str(self.value) + " " + str(self.priority)

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

    def is_empty(self):
      return self.end == -1

    def reheap_up(self, index):
      if index == 0: return
      parent = (index - 1) // 2
      if self.arr[index] < self.arr[parent]:
        self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
        self.reheap_up(parent)
    
    def reheap_down(self, index):
      left = 2 * index + 1
      right = 2 * index + 2
      if left > self.end: return # left doesnt exist
      elif right > self.end: # right doesnt exist
        if self.arr[index] > self.arr[left]: # if parent greater than left
          self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
          self.reheap_down(left)
      else: # left and right both exist
        if self.arr[left] < self.arr[right]: # which is lower - left or right, if left is lower
          if self.arr[index] > self.arr[left]: # if paretn is greater than left
            self.arr[index], self.arr[left] = self.arr[left], self.arr[index]
            self.reheap_down(left)
        else: # if right is greater
          if self.arr[index] > self.arr[right]: # if parent is greater than right
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

  def __init__(self, name, value=None):
    self.value = value
    self.name = name
    self.parent = None
    self.cost_from_source = math.inf
  
  def __eq__(self, __o):
    return self.name == __o.name

class Graph:

  def __init__(self):
    self.adjacency_list = {}
    self.vertices = {}
    self.weights = {}
  
  def add_undirected_edge(self, v1, v2, weight=1):
    #if v1.name == v2.name: return
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
      if v2.name in self.weights[v1.name]:
        if weight < self.weights[v1.name][v2.name]: self.weights[v1.name][v2.name] = weight
      self.weights[v1.name][v2.name] = weight
    else:
      self.weights[v1.name] = {v2.name: weight}
    
    if v2.name in self.weights:
      if v1.name in self.weights[v2.name]:
        if weight < self.weights[v2.name][v1.name]: self.weights[v2.name][v1.name] = weight
      self.weights[v2.name][v1.name] = weight
    else:
      self.weights[v2.name] = {v1.name: weight}
  
  def add_directed_edge(self, v1, v2, weight=1):
    #if v1.name == v2.name: return
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
      if v2.name in self.weights[v1.name]:
        if weight < self.weights[v1.name][v2.name]: self.weights[v1.name][v2.name] = weight
      else:
        self.weights[v1.name][v2.name] = weight
    else:
      self.weights[v1.name] = {v2.name: weight}

def a_star(graph, heuristic_table, source, destination):
  for vertices in graph.vertices:
    graph.vertices[vertices].cost_from_source = math.inf
    graph.vertices[vertices].parent = None
  
  priority_queue = MinHeap()

  source.cost_from_source = 0

  priority_queue.enqueue(PriorityNode(source, 0))

  while not priority_queue.is_empty():
    current = priority_queue.dequeue()
    current = current.value
    if current == destination:
      return current.cost_from_source
    for neighbor in graph.adjacency_list[current.name]:
      neighbor = graph.vertices[neighbor]
      if neighbor.cost_from_source > current.cost_from_source + graph.weights[current.name][neighbor.name]:
        neighbor.cost_from_source = current.cost_from_source + graph.weights[current.name][neighbor.name]
        neighbor.parent = current
        priority_queue.enqueue(PriorityNode(neighbor, neighbor.cost_from_source + heuristic_table[neighbor.name]))
  
  return None
      

if __name__ == "__main__":
  graph = Graph()

  s = Vertex("S")
  a = Vertex("A")
  b = Vertex("B")
  d = Vertex("D")

  graph.add_directed_edge(s, a, 1)
  graph.add_directed_edge(s, b, 3)
  graph.add_directed_edge(a, b, 1)
  graph.add_directed_edge(s, s, 3)
  graph.add_directed_edge(a, d, 4)
  graph.add_directed_edge(b, d, 1)
  graph.add_directed_edge(b, d, 6)
  graph.add_directed_edge(b, s, 4)
  graph.add_directed_edge(a, a, 5)
  # graph.add_directed_edge(a, a, 5)


  heuristics2 = {
    "S": 3,
    "A": 2,
    "B": 1,
    "D": 0
  }

  heuristics1 = {
    "S": 8,
    "A": 3,
    "B": 7,
    "D": 2
  }

  # for i, heuristic_table in enumerate([heuristics1, heuristics2]):
  #   a_star_result = a_star(graph, heuristic_table, s, g)
  #   print(f"Using Heuristic {i+1}:")
  #   if a_star_result is not None:
  #     print(f"Path Cost: {a_star_result}")
  #     c = g
  #     path = []
  #     while c.parent is not None:
  #       path.append(c.name)
  #       c = c.parent
  #     path.append(c.name)
  #     print(f"Path: {path[::-1]}")
  #   else:
  #     print("No path found")

  #   print("\n")

  res = a_star(graph, heuristics2, s, d)

  c = d
  path = []
  while c.parent is not None:
    path.append(c.name)
    c = c.parent
  path.append(c.name)
  print(graph.adjacency_list)
  print(graph.weights)
  print(path)