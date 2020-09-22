"""
Also, try solving the islands matrix problem:
Write a function that takes a 2D binary array and returns the number of 1 islands. 

An island consists of 1s that are connected to the north, south, east or west. 
Or a 1 all by itself.

For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

Describe in graphs terminology
- "island"?
- 1 or a 0?
- When are nodes connected?

Approaches to solve!
- Stuck!
"""
big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def getNeighbors(matrix, node):

    row, col = node

    neighbors = []

    if col > 0 and matrix[row][col - 1] > 0:
        neighbors.append((row, col - 1))

    if col < len(matrix) - 1 and matrix[row][col + 1] > 0:
        neighbors.append((row, col + 1))

    if row < len(matrix) - 1 and matrix[row + 1][col] > 0:
        neighbors.append((row + 1, col))

    if row > 0 and matrix[row - 1][col] > 0:
        neighbors.append((row - 1, col))

    return neighbors


def dft_recursive(node, matrix, visited):
    if node not in visited:
        visited.add(node)
        neighbors = getNeighbors(matrix, node)
        for neighbor in neighbors:
            dft_recursive(neighbor, matrix, visited)


def island_counter(matrix):
    visited = set()
    total_islands = 0
# Iterate over every item
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
    # If it's a 1 and hasn't been visited:
            item = matrix[row][col]
            if item == 1 and (row, col) not in visited:
                total_islands += 1
        #    run a traversal
                dft_recursive((row, col), matrix, visited)

    return total_islands

print(island_counter(islands)) # returns 4
print(island_counter(big_islands)) # returns 13