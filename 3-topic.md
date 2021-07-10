<!-- Provide the tutorial for the third data structure topic. You should include a link back to the welcome page. -->

## Tree
A Binary Tree is a non-linear data structure that is used for searching and data organization. A binary tree is comprised of nodes. Each node being a data component, one a left child and the other the right child.

![Tree Image](https://github.com/travis7smith/CSE212_final/blob/main/Picture%20Files/tree.png?raw=true)

### Input
```sh
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
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
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
When the above code is executed, it pr
```
### Output
```sh
3 6 12 14
```
* Problem to solve (TODO)

### [Link to Welcome Page](https://travis7smith.github.io/CSE212_final/)