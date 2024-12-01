# Submoudles imported
import distance_calculator
import load_data
import create_graph
import plot_graph
import logger



# Standard library imports
import os

# Global Constants
INITIAL_POSITION = 0
INITIAL_VISITED_NODES = [INITIAL_POSITION]

def main():
    # Load JSON files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path_locations = os.path.join(current_dir, "locations.json")
    json_file_path_mode = os.path.join(current_dir, "mode_of_transport.json")
    locations = load_data.load_from_json(json_file_path_locations)
    mode_of_transport = load_data.load_from_json(json_file_path_mode)

    if locations:
        visited_nodes, transport_list = distance_calculator.calculate_distance(INITIAL_POSITION, INITIAL_VISITED_NODES, locations, mode_of_transport)
        logger.log_message("Visited nodes: " + str(visited_nodes), visited_nodes)
        G = create_graph.create_graph(visited_nodes, locations)
        plot_graph.plot_graph(G, visited_nodes, locations, transport_list)
    else:
         print("No locations data available. Please check the JSON file.")
    
if __name__ == "__main__":
    main()
