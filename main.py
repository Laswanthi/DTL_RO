from graph_module import Graph
from route_optimizer import RouteOptimizer
from input_module import get_route_input
from output_module import display_output

def main():
    graph_obj = Graph()

    route_list, start, end = get_route_input()

    for source, destination, distance in route_list:
        graph_obj.add_route(source, destination, distance)

    optimizer = RouteOptimizer(graph_obj.get_graph())

    distance, path = optimizer.shortest_path(start, end)

    display_output(distance, path)

if __name__ == "__main__":
    main()