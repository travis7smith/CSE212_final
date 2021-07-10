<!-- Provide the tutorial for the first data structure topic. You should include a link back to the welcome page. -->

## Queue
Queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first. Or another example we are all familiar with is queuing songs to listen to.

![Queue Image](https://github.com/travis7smith/CSE212_final/blob/main/Picture%20Files/queue.png?raw=true)

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
* Problem to solve (TODO)

### [Link to Welcome Page](https://travis7smith.github.io/CSE212_final/0-welcome.html)
