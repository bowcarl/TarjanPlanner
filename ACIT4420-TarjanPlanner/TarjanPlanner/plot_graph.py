import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define a mapping from transport modes to colors
transport_mode_colors = {
    "bus": "blue",       # Bus edges will be blue
    "train": "green",    # Train edges will be green
    "bicycle": "yellow", # Bicycle edges will be yellow
    "walking": "red"     # Walking edges will be red
}

def plot_graph(G, visited_nodes, locations, transport_list):
    # Ensure the first node is the start/stop node
    visited_locations = [locations[0]] + [locations[i] for i in visited_nodes[1:]]  # Include start node first

    # Create a position dictionary based on Latitude and Longitude for visited nodes
    pos = {i: (street['Longitude'], street['Latitude']) for i, street in enumerate(visited_locations)}

    plt.figure(figsize=(12, 12))

    # Labels for nodes (Street Names)
    labels = {i: visited_locations[i]['Street_Name'] for i in range(len(visited_locations))}

    # Draw nodes (excluding the start node for now)
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=[i for i in range(1, len(visited_locations))],  # Exclude the start node
        node_size=700,
        node_color="skyblue",
        alpha=0.7
    )

    # Draw the start node as a green square
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=[0],  # Only the start node
        node_size=700,
        node_color="green",
        node_shape="s",  # Square shape
        alpha=0.7
    )

    # Map transport modes to edge colors
    edge_colors = [transport_mode_colors.get(mode, "gray") for mode in transport_list[:len(visited_nodes) - 1]]

    # Draw edges with colors based on the transport list
    nx.draw_networkx_edges(
        G,
        pos,
        width=2,
        alpha=0.6,
        edge_color=edge_colors  # Color edges based on transport list
    )

    # Draw node labels with street names
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold', font_color="black")

    # Annotate nodes with custom labels
    for i, node in enumerate(visited_nodes):
        # Get the coordinates of the current node
        x, y = pos[i]

        # Adjust y to move the text upwards slightly
        y_offset = 0.002  # Change this value to adjust the vertical position

        # Label the start node (node 0) as 'Start/Stop' in red
        if i == 0:
            plt.text(x, y + y_offset, "Start/Stop", fontsize=12, ha='center', color='red', fontweight='bold')
        else:
            # Find the relative index (using the 'Relative' key in the JSON)
            relative_index = locations[visited_nodes[i]].get('Relative', None)

            if relative_index:
                plt.text(x, y + y_offset, f"Relative {relative_index}", fontsize=12, ha='center', color='darkblue', fontweight='bold')

        # Create legend
    legend_patches = [
        Patch(facecolor='green', label="Start/Stop", edgecolor='black', linewidth=0.5),
        Patch(facecolor='skyblue', label="Relatives", edgecolor='black', linewidth=0.5),
    ] + [Patch(facecolor=color, label=mode.capitalize()) for mode, color in transport_mode_colors.items()]

    plt.legend(
        handles=legend_patches,
        loc="upper left",
        fontsize=10,
        title="Mode of Transport"
    )

    # Add title and remove axes
    plt.title("Tarjan's Travel Plan")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()
