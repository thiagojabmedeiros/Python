stack = []
stack.append(1) # append = push O(1)
stack.append(2) # O(1)
stack.append(3) # O(1)
stack.append(4) # O(1)
stack.append(5) # O(1)
stack.pop() # O(1) - removes 5
print(stack.pop()) # O(1) the pop function removes tha last element in the array and returns it - removes 4
print(stack)