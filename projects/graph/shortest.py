from util import Queue
import time


f = open('words.txt', 'r')
word_list = f.read().split("\n")
f.close()


def get_neighbors(word_set, target):
    neighbors = []
    for index in range(len(target)):
        start = target[:index]
        end = target[index+1:]
        neighbor = [word for word in word_set if word.startswith(
            start) and word.endswith(end)]
        neighbors.extend(neighbor)
    return neighbors


def shortest_transformation(begin_word, end_word):
    if len(begin_word) != len(end_word):
        raise Exception("Length of words do not match")

    words = set([word.lower()
                 for word in word_list if len(word) == len(end_word)])
    # Create an empty queue and enqueue A PATH TO starting vertext ID
    queue = Queue()
    queue.enqueue([begin_word])
    # Create an empty Set to store visited vertices
    visited = set()
    # While the que is not empty..
    while queue.size() > 0:
            # Deqeue the first PATH
        path = queue.dequeue()
        vertex = path[-1]
        # Grab last vertex from the PATH
        # If that vertex hasn't been visited..
        if vertex not in visited:
            if vertex == end_word:
                return path
            # Mark it as visited
            # print(vertex)
            visited.add(vertex)
            # Then add A PATH to its neighbors to the back of the queue
            for neighbor in get_neighbors(words, vertex):
                # COPY THE PATH
                new_path = path.copy()
                # APPEND THE NEIGHBOR TO THE BACK
                new_path.append(neighbor)
                queue.enqueue(new_path)
    return "There is no such transformation sequence"


start_time = time.time()
begin_word = "sail"
end_word = "boat"
print(shortest_transformation(begin_word, end_word))
print(f"Time: {time.time() - start_time: .3f} sec")
