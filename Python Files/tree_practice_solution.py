class Node:

# Create the starting node
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Compare the new value with the parent node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(6)
root.insert(10)
root.insert(467)
root.insert(1)

root.PrintTree()

'''
1
6
10
467
'''