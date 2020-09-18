"""
How to Solve (Almost) Any Graphs Problem

1. Describe the problem using graphs terminology
- What are your nodes?
- What are your edges? aka when is a node connected to another node?
- Are there connected components?

2. Build your graph OR write your getNeighbors() function

3. Choose your algorithm
- BFT, DFT, BFS, DFS



Given two words (begin_word and end_word), and a dictionary's word list, 
return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

return None if it can't be done
all words are lowercase (or you can make them lowercase)

'hit' --> 'hot' --> 'hog'  --> 'cog'
'sail' --> 'bail' --> 'boil' --> 'boat'

1. Graphs terminology
- Nodes: words!
- Edges: a word is connected to another word if they share all letters except one

2. getNeighbors - graph optional

3. Choose algorithm: BFS
"""
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

import string
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# Put our words in a set for O(1) lookup
word_set = set()
for word in words:
      word_set.add(word.lower())


def find_neighbors_alt(word):
    neighbors = []
    ## for every letter in the word, substitute a letter of the alphabet: O(len(word) * 26)
    for i in range(len(word)):
        for alpha_letter in string.ascii_lowercase:
            # one-liner, but it gives different but correct result :thinking_face:
            # maybe_neighbor = word.replace(word[i], alpha_letter, 1)
            # turn word into list
            word_list = list(word)
            word_list[i] = alpha_letter
            ## turn back into string
            maybe_neighbor = "".join(word_list)

            if maybe_neighbor in word_set and maybe_neighbor != word:
                neighbors.append(maybe_neighbor)
    return neighbors


    ## check if this new word is in our giant word list: O(1)
    ## if so, it's a neighbor!

def find_neighbors(node_word, same_length_words):
    ## find all words that are the same length
    matches = []

    ## count how many letters are the same to see if each word is an edge
    for word in same_length_words:
        count = 0
        for i in range(0, len(word)):
            if word[i] == node_word[i]:
                count += 1
        if count == len(node_word) - 1:
            matches.append(word)
    return matches
## sorry for the crappy variable names, we were in a hurry!

def bfs(start_word, end_word):
    # same_length_words = [word for word in word_set if len(word) == len(start_word)]

    q = Queue()
    visited = set()

    # enqueue something...
    q.enqueue([start_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visited:
            visited.add(current_word)

            # neighbors = find_neighbors(current_word, same_length_words)
            neighbors = find_neighbors_alt(current_word)

            for neighbor in neighbors:
                # returns a new list: current_path + [neighbor] 
                path_copy = list(current_path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

print(bfs('hit', 'cog'))
print(bfs('sail', 'boat'))
print(bfs('hungry', 'happy')) # should return None