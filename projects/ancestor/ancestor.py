
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            #add row
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #uses this because of add_vertex
        self.vertices[v1].add(v2)


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        #adds parent
        graph.add_vertex(parent)
        #adds child
        graph.add_vertex(child)
        #add edges from child to parent
        graph.add_edge(child, parent)

    #BFS
    queue = Queue()
    #path of starting node
    queue.enqueue( [starting_node ])


    # Farthest distance from the input individual.
    longest_path_length = 1
    # Has no parents, the function should return -1
    # If there is more than one ancestor tied for "earliest"
    earliest_ancestor = -1
    # While the queue is not empty
    while queue.size() > 0:
        # dequeue the first path
        # Since creating a path, order matters
        path = queue.dequeue()
        # returns -1 if there is no grandparent
        current_node = path[-1]


        #keeps track of longest path with the earliest ancestor or if the path length is greater than the longest path
        if len(path) >= longest_path_length and current_node < earliest_ancestor or len(path) > longest_path_length: 
            # if current_node < earliest_ancestor: #or len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        #from add_edge won't need to create a helper function
        neighbors = graph.vertices[current_node]
        # push (add) path to all neighbors
        for ancestor in neighbors:
            # make a copy of the path
            path_copy = list(path)
            # add the copied path to the neighbor
            path_copy.append(ancestor)
            queue.enqueue(path_copy)

    print(path)
    print(earliest_ancestor)
    return earliest_ancestor


if __name__ == "__main__":
    ancestor = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(ancestor,3))