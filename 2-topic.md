<!-- Provide the tutorial for the second data structure topic. You should include a link back to the welcome page. -->

## Set
__What is a set?__ Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage. A set is a collection which is both unordered and unindexed.

## Properties of a set:
- Sets are unordered
- Set elements are unique, meaning no duplicates
- A Set can be modified but the elements inside must be an unchanging type

![Set Image](https://github.com/travis7smith/CSE212_final/blob/main/Picture%20Files/set.jpg?raw=true)

## Set's Operations:
- __add():__ Adds an element to the set
- __clear():__ Removes all the elements from the set
- __copy():__ Returns a copy of the set
- __pop():__ Removes an element from the set
- __remove():__ Removes the specified element

## Example of a Set in Python
### Input
```sh
# Create the set and claim elements
my_set = {1, 2, 3}
print(my_set)

# A set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
```
### Output
```sh
{1, 2, 3}
{1.0, (1, 2, 3), 'Hello'}
```
## Pros of using a Set:
- Efficient in removing duplicates
- Good with simple math otherations as well as intersections and unions

## Cons of using a Set:
- A set is unordered
- Data inputted must be immuatable, because once added they cannot be changed

## Efficiency:

| Operation | Average Case |
| :--- | ---: |
| Copy | O(n) |
| Append | O(1) |
| Pop last | O(1) |
| Pop intermediate | O(n) |
| Insert | O(n) |
| Delete | O(n) |
| Length | O(1) |
| Get item | O(1) |
| Set item | O(1) |

## Problem to solve
```sh
Start set
{1, 2, 3}

End set
{2, 4, 'fish'}
```
Hint: Study how add() and remove() work and how that could help achieve the deired end output

[Example code](https://github.com/travis7smith/CSE212_final/blob/main/Python%20Files/set_practice_solution.py)

### [Link to Welcome Page](https://travis7smith.github.io/CSE212_final/0-welcome.html)
