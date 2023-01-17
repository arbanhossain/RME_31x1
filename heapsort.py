from DS import MaxHeap, MinHeap

arr = [5,7,89,1,322,4,6,0,-1,63]

# Ascending order
new = []
heap = MinHeap()

for i in arr:
  heap.enqueue(i)
for _ in range(len(arr)):
  new.append(heap.dequeue())

print(new)

# Descending order
new = []
heap = MaxHeap()

for i in arr:
  heap.enqueue(i)
for _ in range(len(arr)):
  new.append(heap.dequeue())

print(new)