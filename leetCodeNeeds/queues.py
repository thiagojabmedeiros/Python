from collections import deque
queue = deque()
queue.append(1) # O(1)
queue.append(2) # O(1)
queue.append(3) # O(1)
queue.append(4) # O(1)
queue.append(5) # O(1)
queue.popleft() # O(1) - removes 1
print(queue.popleft()) # O(1) this pop function removes the first element on left side of the queue and returns it - removes 2
print(queue)