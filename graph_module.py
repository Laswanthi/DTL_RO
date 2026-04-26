class Graph:
    def __init__(self):
        self.graph = {}

    def add_route(self, source, destination, distance):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []

        self.graph[source].append((destination, distance))
        self.graph[destination].append((source, distance))

    def get_graph(self):
        return self.graph