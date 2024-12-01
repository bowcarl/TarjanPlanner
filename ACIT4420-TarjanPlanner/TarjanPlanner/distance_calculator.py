from geopy.distance import geodesic
import itertools
from get_mode import get_mode_of_transport
from track_time import time_this

@time_this
def calculate_distance(current_position, visited_nodes, locations, transport_data):
    
    # Calculate distances between all pairs of locations
    distances = {}
    for i, loc1 in enumerate(locations):
        distances[i] = {}
        for j, loc2 in enumerate(locations): 
            if i != j: # Skip same location
                loc1_coordinates = (loc1['Latitude'], loc1['Longitude'])
                loc2_coordinates = (loc2['Latitude'], loc2['Longitude'])
                distances[i][j] = geodesic(loc1_coordinates, loc2_coordinates).meters

    if len(visited_nodes) == len(locations):
        total_distance = sum(distances[visited_nodes[i]][visited_nodes[i + 1]]
                             for i in range(len(visited_nodes) - 1))
        total_distance += distances[visited_nodes[-1]][visited_nodes[0]]
        print(f"Total distance: {total_distance:.2f} meters")
        return visited_nodes + [visited_nodes[0]], []

    unvisited_nodes = [i for i in range(len(locations)) if i not in visited_nodes] # Get unvisited nodes
    permutations = itertools.permutations(unvisited_nodes)

    min_distance = float('inf')
    best_route = None

    # Try all permutations of unvisited nodes
    for perm in permutations:
        route = [current_position] + list(perm) + [current_position] # Start and end at the current position
        total_distance = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route

    total_time = 0
    total_cost = 0
    transport_list = []

    for i in range(len(best_route) - 1):
        current_node = best_route[i]
        next_node = best_route[i + 1]
        distance_km = distances[current_node][next_node] / 1000

        mode_of_transport = input(
            f"Traveling from {locations[current_node]['Street_Name']} to {locations[next_node]['Street_Name']} "
            f"({distance_km:.2f} km).\n Choose a mode of transport (Bus, Train, Bicycle, Walking): "
        ).strip().lower()

        vehicle, transport_list = get_mode_of_transport(transport_data, mode_of_transport, transport_list)

        travel_time = vehicle.calculate_time(distance_km)
        travel_cost = vehicle.calculate_cost(distance_km)

        total_time += travel_time
        total_cost += travel_cost

        print(f"Mode: {vehicle.mode}, Distance: {distance_km:.2f} km, "
              f"Time: {travel_time:.2f} min, Cost: {travel_cost:.2f} South Korean won")
        print("\n")

    print(f"\nShortest route: {best_route}")
    print(f"Total distance: {min_distance:.2f} meters")
    print(f"Total travel time: {total_time:.2f} minutes")
    print(f"Total travel cost: {total_cost:.2f} South Korean won")
    return best_route, transport_list
