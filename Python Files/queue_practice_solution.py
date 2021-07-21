# Initializing a queue
queue = []
 
# Fill Queue to achieve desired start
queue.append('1')
queue.append('2')
queue.append('3')
 
print("Initial queue")  #Initial queue
print(queue)            #['1', '2', '3']

# Append and pop as needed to achieve desired end
queue.pop(0)
queue.append('5')
queue.append('fish')
 
print("\nEnd queue")    #End queue
print(queue)            #['1', '3', '5', 'fish']