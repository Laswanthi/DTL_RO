def get_route_input():
    routes = int(input("Enter number of routes: "))
    route_list = []

    for _ in range(routes):
        source = input("Enter source: ")
        destination = input("Enter destination: ")
        distance = int(input("Enter distance: "))
        route_list.append((source, destination, distance))

    start = input("Enter start location: ")
    end = input("Enter destination location: ")

    return route_list, start, end