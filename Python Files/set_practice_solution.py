# Create the set
set = {1, 2, 3}
print('Start set')
print(set)

# Using add() and remove() as need to achieve the desired output
set.remove(1)
set.remove(3)
set.add(4)
set.add('fish')

print('\nEnd set')
print(set)

'''
Start set
{1, 2, 3}

End set
{2, 4, 'fish'}
'''