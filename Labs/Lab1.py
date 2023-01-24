class Node:

  def __init__(self, elem):
    self.value = elem
    self.next = None

class Queue:

  def __init__(self):
    self.head = None
    self.tail = None

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

class Vertex:

  def __init__(self, name, value=None):
    self.value = value
    self.name = name

# Space: O(V) for vertices. O(E) for edges. Total O(V+E)
class Graph:

  def __init__(self):
    self.adjacency_list = {}
    self.vertices = {}
  
  def add_directed_edge(self, v1, v2):
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
  
  # Time: O(V+E)
  # Space: O(V)
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

if __name__ == "__main__":
  no_of_vertices, edges, source = map(int, input().split())
  
  graph = Graph()

  for _ in range(edges):
    v1, v2 = [Vertex(x) for x in input().split()]
    graph.add_directed_edge(v1, v2)
  
  for _ in range(int(input())):
    v1, v2 = [x for x in input().split()]
    print(graph.path_exists_bfs(v1, v2))