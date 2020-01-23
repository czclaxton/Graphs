import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        total_friendships = avg_friendships * num_users // 2

        for i in range(total_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        queue = Queue()
        queue.enqueue([user_id])
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        while queue.size() > 0:
            path = queue.dequeue()

            v = path[-1]

            if v not in visited:
                visited[v] = path

                for friend_id in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    queue.enqueue(path_copy)

        return visited


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


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('HERE1', sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('HERE2', connections)
