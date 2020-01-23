from graph import Graph
from util import Stack, Queue

# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# island_counter(islands) # returns 4
# connected - has edges, connected components
# array/2d
#n, s, e, w
#binary - values
# island/1 islands = connected components
#  return 1 islands - number of connect components


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def island_counter(islands):
    graph = Graph()
    for island in islands:
        for v in island:
            graph.add_vertex((island.index(), ind.index()))


island_counter(islands)  # returns 4
