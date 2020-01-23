import sys


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for i in range(1, 12):
        graph.add_vertex(i)
    for pair in ancestors:
        graph.add_edge(pair[0], pair[1])

    queue = Queue()
    queue.enqueue(starting_node)

    check_num = ''

    # print(graph.vertices)
    # print(f'STARTING NODE {starting_node}')
    check_arr = []
    children = []
    for i in graph.vertices:
        if graph.vertices[i] != set():
            while len(graph.vertices[i]) > 0:
                check_num = graph.vertices[i].pop()

                check_arr.append((check_num, i))
                # print(f'CHECK_NUM = {check_num}')
                children.append(check_num)
                # print(f'CHECK_ARR = {check_arr}')

    # print(check_arr)
    for i in check_arr:
        if i[0] == starting_node:
            # print(f'found it at {i[1]} and it does equal {starting_node}')
            if i[1] in children:
                # print(f'pass in {i[1]}')
                return earliest_ancestor(ancestors, i[1])
            else:
                return i[1]
    return -1


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbors = []
        for neighbor in self.vertices[vertex_id]:
            neighbors.append(neighbor)
        return neighbors

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)

        visited = set()

        while queue.size() > 0:
            vertex = queue.dequeue()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for i in self.vertices[vertex]:
                    queue.enqueue(i)
        print('**** End ****')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        stack = Stack()
        stack.push(starting_vertex)

        visited = set()

        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)
        print('**** End ****')

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])

        visited = set()

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        path = []
        visited = {starting_vertex}
        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()
            path.append(vertex)

            for v in self.vertices[vertex]:
                stack.push(v)
                visited.add(v)

                if v == destination_vertex:
                    path.append(v)
                    return path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if not visited:
            visited = set()

        if not path:
            path = []

        visited.add(starting_vertex)
        # path = path + [starting_vertex]
        path.extend(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None


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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
