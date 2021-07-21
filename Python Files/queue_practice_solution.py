# Initializing a queue
queue = []
 
# Fill Queue to achieve desired start
queue.append('1')
queue.append('2')
queue.append('3')
 
print("Initial queue")
print(queue)

# Append and pop as needed to achieve desired end
queue.pop(0)
queue.append('5')
queue.append('fish')
 
print("\nEnd queue")
print(queue)

'''
Initial queue
['1', '2', '3']

End queue
['1', '3', '5', 'fish']
'''
