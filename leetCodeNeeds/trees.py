class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            return self.insertChild(self.root, value)
        
    def insertChild(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = Node(value)
            else:
                return self.insertChild(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                return self.insertChild(node.right, value)
    
    def search(self, target):
        return self.searchx(self.root, target)
    
    def searchx(self, node, target):
        if node is None:
            print(False)
            return False
        else:
            if node.value == target:
                print(True)
                return True
            elif node.value > target:
                return self.searchx(node.left, target)
            else:
                return self.searchx(node.right, target)            

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

tree = BinaryTree()
for val in [64,37,12,89,40,90,21,50]:
    tree.insert(val)

inOrder(tree.root)