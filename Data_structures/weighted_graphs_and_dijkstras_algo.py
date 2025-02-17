"""weighted_graphs.py"""


from math import inf



class NaivePriorityQueue:
    """This is a Naive and Simple priority Queue"""

    def __init__(self):
        self.values = []

    def _sort(self):
        self.values.sort(key=lambda x: x["priority"])

    def enqueue(self, value, priority):
        self.values.append({"value": value, "priority": priority})
        self._sort()

    def dequeue(self):
        return self.values.pop(0)


class WeightedGraphs:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex: str):
        """
        This functions adds a vertex into the graphs.
        Args:
            vertex (str): vertex that needs to be added.

        Raises:
            ValueError: when the same vertex is already present.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        else:
            raise ValueError(f"{vertex} already exits in the graph")

    def add_edges(self, vertex_1: str, vertex_2: str, weight: int):
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
            self.adjacency_list[vertex_1].append(
                {"node": vertex_2, "weight": weight})
            self.adjacency_list[vertex_2].append(
                {"node": vertex_1, "weight": weight})
        else:
            raise ValueError(
                f"either '{vertex_1}' or '{vertex_2}' are not present in the graph")

    def remove_edge(self, vertex_1: str, vertex_2: str):
        """
        This function removes the vertices and its edges.
        Args:
            vertex (str): The vertex to be removed.

        Returns:
            graphs
        """
        if vertex_1 in self.adjacency_list and vertex_2 in self.adjacency_list:
            self.adjacency_list[vertex_1] = [
                edge for edge in self.adjacency_list[vertex_1] if edge.get("node") != vertex_2]
            self.adjacency_list[vertex_2] = [
                edge for edge in self.adjacency_list[vertex_2] if edge.get("node") != vertex_1]
        else:
            raise ValueError(
                f"either '{vertex_1}' or '{vertex_2} does not exist!")
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
            for edges in rem_edges:
                self.remove_edge(vertex, edges.get("node"))
            self.adjacency_list.pop(vertex)
        else:
            raise ValueError(f"'{vertex}' could not be found in the graphs")
        return self

    def dfs_transversal(self, start_vertex: str):
        final_list = []
        visited_obj = {}

        def dfs(vertex: str | None):
            if vertex is None:
                return None
            visited_obj[vertex] = True
            final_list.append(vertex)
            for values in self.adjacency_list[vertex]:
                if values["node"] not in visited_obj or visited_obj[vertex] is False:
                    dfs(values["node"])
        dfs(start_vertex)
        return final_list

    def dijkstras_algo(self, start, end):
        nodes = NaivePriorityQueue()
        distances_obj = {}
        previous_obj = {}
        smallest = None
        path = []

        for vertex in self.adjacency_list:
            if vertex == start:
                distances_obj[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances_obj[vertex] = inf
                nodes.enqueue(vertex, inf)
            previous_obj[vertex] = None

        while nodes:
            smallest = nodes.dequeue()["value"]
            if smallest == end:
                while previous_obj[smallest]:
                    path.append(smallest)
                    smallest = previous_obj[smallest]
                break
            if smallest or distances_obj[smallest] is not inf:
                for neighbor in self.adjacency_list[smallest]:
                    # Calculate distance
                    candidate = distances_obj[smallest] + neighbor["weight"]
                    if candidate < distances_obj[neighbor["node"]]:
                        # updating new smallest distance
                        distances_obj[neighbor["node"]] = candidate
                        previous_obj[neighbor["node"]] = smallest
                        # Enqueue
                        nodes.enqueue(neighbor["node"], candidate)
        path.append(start)
        path = list(reversed(path))
        return path
