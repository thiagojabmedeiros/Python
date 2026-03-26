class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.value)
        inOrder(node.right)
def preOrder(node):
    if node:
        print(node.value)
        preOrder(node.left)
        preOrder(node.right)
def postOrder(node):
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.value)

inOrder(root)
print("#######")
preOrder(root)
print("#######")
postOrder(root)