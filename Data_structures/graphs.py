"""graphs.py"""

class Graphs:
    """This is a graphs data structure and all its methods."""

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex: str):
        """
        This function adds a vertex into the graph.
        Args:
            vertex (str): The name of the vertex.

        Raises:
            ValueError: if there already exists vertex by that name.

        Returns:
            graphs
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        else:
            raise ValueError(f"The vertex :: {vertex} already exists.")
        return self

    def add_edges(self, vertex_1: str, vertex_2: str):
        """
        This function creates connects between two vertices.

        Args:
            vertex_1 (str): First vertex
            vertex_2 (str): Second vertex

        Raises:
            ValueError: raised when the the vertices do not exits.

        Returns:
            graphs
        """
        if vertex_1 in self.adjacency_list and vertex_2 in self.adjacency_list:
            self.adjacency_list[vertex_1].append(vertex_2)
            self.adjacency_list[vertex_2].append(vertex_1)
        else:
            raise ValueError(
                f"either {vertex_1} or {vertex_2} does not exists")
        return self

    def remove_edge(self, vertex_1: str, vertex_2: str):
        """
        This function removes connection between two vertices.
        Args:
            vertex_1 (str): First vertex
            vertex_2 (str): Second vertex
        """
        if vertex_1 in self.adjacency_list and vertex_2 in self.adjacency_list:
            self.adjacency_list[vertex_1].remove(vertex_2)
            self.adjacency_list[vertex_2].remove(vertex_1)
        else:
            raise ValueError(f"either {vertex_1} or {vertex_2}")
        return self

    def remove_vertex(self, vertex: str):
        """
        This function removes the vertices and its edges.
        Args:
            vertex (str): The vertex to be removed.

        Returns:
            graphs
        """
        if vertex in self.adjacency_list:
            rem_edges = self.adjacency_list[vertex][:]
            for child_ver in rem_edges:
                self.remove_edge(vertex, child_ver)
            self.adjacency_list.pop(vertex)
        else:
            raise ValueError(f"'{vertex}' does not exits.")
        return self

    def dfs_traversal(self, start_vertex: str):
        """
        This is depth first algo which goes through the graphs recursively.
        Args:
            start_vertex (str): Defined starting point.

        Returns:
            list
        """
        final_list = []
        visited_obj = {}

        def dfs(vertex: str | None):
            if vertex is None:
                return None
            visited_obj[vertex] = True
            final_list.append(vertex)
            for values in self.adjacency_list[vertex]:
                if values not in visited_obj or visited_obj[values] is False:
                    dfs(values)
        dfs(start_vertex)
        return final_list

    def dfs_iterative(self, start_vertex: str):
        """
        This is the dfs function but in an iterative format.
        Args:
            start_vertex (str): Starting point. 

        Returns:
            list.
        """
        final_list = []
        stack = [start_vertex]
        visited_obj = {}
        current_vertex = ""

        visited_obj[start_vertex] = True
        while len(stack) > 0:
            current_vertex = stack.pop()
            final_list.append(current_vertex)

            for values in self.adjacency_list[current_vertex]:
                if values not in visited_obj or visited_obj[values] is False:
                    visited_obj[values] = True
                    stack.append(values)
        return final_list

    def bfs_iterative(self, start_vertex: str):
        """
        This is the breath first search using an iterative loop.
        Args:
            start_vertex (str): Starting point.

        Returns:
            list.
        """
        queue = [start_vertex]
        final_list = []
        visited_obj = {}
        current_vertex = ""

        visited_obj[start_vertex] = True
        while queue:
            current_vertex = queue.pop(0)
            final_list.append(current_vertex)
            for values in self.adjacency_list[current_vertex]:
                if values not in visited_obj or visited_obj[values] is False:
                    visited_obj[values] = True
                    queue.append(values)

        return final_list


