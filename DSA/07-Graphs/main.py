class Graph:
    def __init__(self):
        self.adjacency_list: dict[str, list] = {}

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_vertex(self, vertex: str):
        """
        Adds a vertex to the graph.
        Args:
            vertex: The vertex to be added to the graph.
        Returns:
            bool: True if the vertex was added successfully, False if the vertex already exists.
        Pseudo Code:
        1. Check if the vertex is not already in the adjacency list.
        2. If the vertex is not in the adjacency list:
            a. Add the vertex to the adjacency list with an empty list as its value.
            b. Return True indicating the vertex was added.
        3. If the vertex is already in the adjacency list, return False.
        """

        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        """
        Adds an undirected edge between two vertices in the graph.
        Args:
            v1: The first vertex.
            v2: The second vertex.
        Returns:
            bool: True if the edge was successfully added, False otherwise.
        """

        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
            return True
        return False  # no edge was formed

    def remove_edge(self, v1, v2):
        """
        This method removes the edge between the vertices `v1` and `v2` if both vertices exist in the adjacency list.
        If there is no edge between the vertices, the method will silently handle the ValueError and return True.
        If either vertex does not exist in the adjacency list, the method will return False.
        Args:
            v1: The first vertex.
            v2: The second vertex.
        Returns:
            bool: True if the edge was successfully removed, False otherwise.
        """

        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            try:
                self.adjacency_list[v1].remove(v2)
                self.adjacency_list[v2].remove(v1)
            except ValueError:
                # there is no edge connection between nodes
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        """
        Removes a vertex and all its edges from the graph.
        Args:
            vertex: The vertex to be removed from the graph.
        Returns:
            bool: True if the vertex was successfully removed, False if the vertex was not found in the graph.
        """

        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False


graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

# graph.remove_edge("A", "B")
# graph.remove_edge("A", "D")

graph.remove_vertex("D")

graph.print_graph()
