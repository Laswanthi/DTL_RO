import heapq

class RouteOptimizer:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, end):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            cost, current, path = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)
            path = path + [current]

            if current == end:
                return cost, path

            for neighbor, distance in self.graph[current]:
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (cost + distance, neighbor, path)
                    )

        return float("inf"), []