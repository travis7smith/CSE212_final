<!-- Provide the tutorial for the first data structure topic. You should include a link back to the welcome page. -->

# Queue
__What is a queue?__ A queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first. Or another example we are all familiar with is queuing songs to listen to.

## Properties of a Queue:
- Items that are closer to the front of the queue have been there the longest.
    - FIFO (First in, first out)
- Usually don’t lookup in a queue.
- Best implemented with a linked list. Faster to remove items without shift.
    - Exapmle: Printer queue of documents to be printed, or a queue of people.

![Queue Image](https://github.com/travis7smith/CSE212_final/blob/main/Picture%20Files/queue.png?raw=true)

## Queue's Operations
- __enqeue(e):__ add an element (e) to the back of the queue
- __append():__ same as enqueue, add element to back of queue
- __dequeue():__ removes and returns the first element from queue
- __pop():__ same as dequeue, removes element from queue
- __peek():__ Returns the element at the front of the queue

## Example of a Queue in Python
### Input
```sh
# Initializing a queue
queue = []
 
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
 
print("Initial queue")
print(queue)
 
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nQueue after removing elements")
print(queue) 
```
### Output
```sh
Initial queue
['a', 'b', 'c']

Elements dequeued from queue
a
b
c

Queue after removing elements
[]
```
## Pros of using a Queue:
- Fast operations
- Fast Peek
- Ordered

## Cons of using a Queue:
- Slow lookup

## Effeciency:

| Operation | Average Case |
| :--- | ---: |
| Lookup | O(n) |
| enqueue/append | O(1) |
| dequeue/pop | O(1) |
| peek | O(1) |

## Problem to solve
Create code so that the output will be:
```sh
Initial queue
['1', '2', '3']

End queue
['1','3','5','fish']
```
Hint: Study how append() and pop() work and how that could help achieve the deired end output

[Example code](https://github.com/travis7smith/CSE212_final/blob/main/Python%20Files/queue_practice_solution.py)

### [Link to Welcome Page](https://travis7smith.github.io/CSE212_final/0-welcome.html)
