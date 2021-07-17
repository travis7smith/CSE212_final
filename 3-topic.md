<!-- Provide the tutorial for the third data structure topic. You should include a link back to the welcome page. -->

## Tree
__What is a tree?__ A Binary Tree is a non-linear data structure that is used for searching and data organization. A binary tree is comprised of nodes. Each node being a data component, one a left child and the other the right child.

## Properties of a Tree:
- One node is marked as Root node.
- Every node other than the root is associated with one parent node.
- Each node can have an arbiatry number of child nodes.

![Tree Image](https://github.com/travis7smith/CSE212_final/blob/main/Picture%20Files/tree.png?raw=true)

## Tree's Operations:
- __Node():__ Names the node and its value
- __root.insert():__ Inserts a branch to the tree

## Example of a Tree in Python
### Input
```sh
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
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
```
### Output
```sh
3
6
12
14
```
## Pros of using a Set
- Best for optimize for efficient searching and updates
- Elements are sorted

## Cons of using a Set
- More complexity and maintainence
- Multi-dimentional structure, needs to be mapped out and organized

## Efficiency:

| Operation | Average Case |
| :--- | ---: |
| Searching | O(h) |
| Insertion | O(h) |
| Deletion | O(h) |
h being the height og the tree

## Problem to solve
Create code so that the output is the following:
```sh
1
6
10
467
```
Hint: Study how insert() works and how that could help achieve the deired end output. Also look at the example how the sets up how to create a tree

[Example code](https://github.com/travis7smith/CSE212_final/blob/main/Python%20Files/tree_practice_solution.py)

### [Link to Welcome Page](https://travis7smith.github.io/CSE212_final/0-welcome.html)
