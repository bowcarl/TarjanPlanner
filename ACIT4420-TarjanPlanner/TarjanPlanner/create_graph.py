import get_visited_locations
import networkx as nx
from geopy.distance import geodesic

def create_graph(visited_nodes, locations):
    visited_locations = get_visited_locations.get_visited_locations(visited_nodes, locations)
    G = nx.Graph()

    for i in range(len(visited_locations) - 1):
        node = i
        next_node = i + 1

        loc1 = (visited_locations[node]['Latitude'], visited_locations[node]['Longitude'])
        loc2 = (visited_locations[next_node]['Latitude'], visited_locations[next_node]['Longitude'])

        G.add_node(node, label=visited_locations[node]['Street_Name'])
        G.add_node(next_node, label=visited_locations[next_node]['Street_Name'])

        distance = geodesic(loc1, loc2).meters
        G.add_edge(node, next_node, weight=distance)

    return G