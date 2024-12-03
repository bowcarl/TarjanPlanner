# ACIT4420-TarjanPlanner

This program is created as a part of the course ACIT4420. The **ACIT4220-TarjanPlanner** is a tool created to calculate the shortest distance, and based on selected modes of transportation, calculate time and cost for Tarjan to visit his ten relatives. The package includes nine python files: **calculate_distance.py**, **load_data.py**, **get_visited_location.py**, **get_mode.py**, **logger.py**, **plot_graph.py**,**track_time.py** and **vechile.py**. Additonaly the program has a `__main__.py` entrypoint, an `__init__.py` file to mark it as module, a **log_message.txt** file for logging, **locations.json** file were the location information are stored and **mode_of_transport.json** were speed, transfer time and cost is factored in.

## Table of Contents
- [Features](#features)
- [Installation Manual](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Files](#key-files)
- [License](#license)
  
## Features
- Calculate the shortest path to take given a location list
- Caclulate the total distance for the shortest path
- Calculate the total time given the mode of transport
- Calculate the total cost given the mode of transport
- Illustrate the decipted route as a graph with colors
- Modular design for easy extension and maintenance.
- Adaptable code, easy to add or remove locations
  
## Installation Manual

Follow these simple steps to install and set up the project:

1. **Clone the Repository**

Firstly, clone the repository from GitHub (or download the package manually):

```bash
git clone https://github.com/bowcarl/TarjanPlanner.git
cd TarjanPlanner
```
2. **Create a virtual environment**

Furthermore, It's recommended to create a virtual environment to isolate the project dependencies. Continue and run the following commands:

```bash
python3 -m venv tarjanenv
source tarjanenv/bin/activate # or with windows use `tarjanenv\Scripts\activate`
```

3. **Install the Package**

With your virtual environment set up, install the project using the pip tool:

```bash
pip install -e .
```

## Usage
Once the package is installed you only need to run this command in your preffered terminal:
```bash
TarjanPlanner
```
This will ask you for a several inputs choosing a transportation mode between each location.
Simply decide upon your preffered transportation modes, and then the program will display the graph with color corresponding the your choices. In the terminal you will also see the visted nodes, total travel time, total distance and cost of the journey.

## Project Structure
```
ACIT4420-TarjanPlanner/
│
├── TarjanPlanner/
|   ├── __pyache__.py
|       ├── (...).py
│   ├── __init__.py
│   ├── __main__.py                # Entry point for the module
│   ├── create_graph.py
│   ├── distance_calculator.py
|   ├── get_mode.py
│   ├── get_visited_locations.py
│   ├── load_data.py
|   ├── logger.py
|   ├── message_log.txt
|   ├── mode_of_transport.json
│   ├── plot_graph.py
│   ├── locations.json
│   ├── track_time.py
│   └── vechile.py
│
├── setup.py                   # Installation script
└── README.md                  # Project documentation (this file)
```
### Key Files
- **`__main__.py`**: Contains the main function that launces the option menu.
- **`setup.py`**: Scripts for installing the package.
- **`distance_calculator.py`**: Calculates shortest distance
- **`get_mode.py`**: Quirres transportation modes
- **`load_data.py`**: Loads JSON data
- **`get_visited_locations.py`**: Gets visited locations
- **`vehicle.py`**: Class used to calculate time and cost
- **`logger.py`**: Logs visited nodes to a text file
- **`create_graph.py`**: Creates the nodes and edges
- **`plot_graph.py`**: Styles the graph
- **`track_time.py`**: Tracks execution time

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/shailendrabhandari/project_game/blob/main/LICENSE) file for details.

