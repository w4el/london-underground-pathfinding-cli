# Import necessary classes and modules
from Graph import Graph_count_stations  # Importing Graph_count_stations class from Graph module
from bellman_ford import bellman_ford  # Import the Bellman-Ford algorithm implementation
import os
# Define a class to assist in finding station names and tube lines on the graph
class StationLineFinder:
    # Constructor for the class that takes a graph object as an argument
    def __init__(self, graph):
        self.graph = graph  # Storing the graph object for later use

    # Method to find the exact name of a station given a possible partial or case-insensitive name
    def find_station_name(self, station_name):
        # Iterate through all station names in the graph
        for real_name in self.graph.stations:
            # Check if the provided name matches any station name in the graph, ignoring case
            if station_name.lower() == real_name.lower():
                return real_name  # Return the exact station name if found
        return None  # Return None if no exact match is found

    # Method to get the index of a station from a given prompt
    def get_station_index(self, station_name_prompt):
        while True:
            station_name = input(station_name_prompt).strip().title()  # Prompt the user for the station name and format it
            matched_station = self.find_station_name(station_name)  # Find the exact station name
            if matched_station:
                return self.graph.station_to_int[matched_station]  # Return the index of the station if found
            print("Station not found. Please check the name and try again.")  # Prompt again if not found

    # Method to find the tube line connecting two stations
    def get_tube_line(self, station1, station2):
        # Return the tube line connecting the two stations (in either direction)
        return self.graph.tube_lines.get((station1, station2)) or self.graph.tube_lines.get((station2, station1))

# Define a class for finding the shortest path between two stations using Bellman-Ford algorithm
class ShortestPathFinder:
    # Constructor for the class that takes a StationLineFinder object as an argument
    def __init__(self, station_finder):
        self.station_finder = station_finder  # Storing the station finder object for later use

    # Method to find and print the shortest path between two stations
    def find_and_print_shortest_path(self, line):
        # Get the indices of the start and destination stations from user input
        source_index = self.station_finder.get_station_index("Enter the start station: ")
        destination_index = self.station_finder.get_station_index("Enter the destination station: ")
        
        # Run Bellman-Ford algorithm to find the shortest path and its distance
        distances, predecessors, no_negative_cycle = bellman_ford(self.station_finder.graph.graph, source_index)

        # Check for negative weight cycles
        if not no_negative_cycle:
            print("A negative-weight cycle detected. Cannot find shortest path.")
            return

        # Prepare lists to display the path and count the number of stations
        display_path = [self.station_finder.graph.int_to_station[destination_index]]
        count_path = [self.station_finder.graph.int_to_station[destination_index]]

        current_station = destination_index
        previous_line = None  # Variable to track line changes in the path

        # Loop to construct the path using the predecessors
        while predecessors[current_station] is not None:
            next_station = predecessors[current_station]
            line = self.station_finder.get_tube_line(next_station, current_station)  # Get the tube line for this path segment

            # Handle line changes in the path display
            if previous_line is not None and line != previous_line:
                display_path.insert(1, f"(Switch to {previous_line} line at {self.station_finder.graph.int_to_station[current_station]})")
            
            current_station = next_station
            display_path.insert(0, self.station_finder.graph.int_to_station[current_station])
            count_path.insert(0, self.station_finder.graph.int_to_station[current_station])  # Add station to count path
            previous_line = line

        # Count the number of stations in the path
        stations_count = len(count_path)

        # Print the shortest path and the total number of stations on the path
        print("Shortest path (by number of stations):", " -> ".join(display_path))
        print(f"Total stations in the path: {stations_count} stations")

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    # Define the file path for the London Underground data set
    file_path = os.path.join(parent_dir, r"Data sets\London Underground data with times only.xlsx")
    # Create a graph object for the London Underground using the provided file path
    london_underground_graph = Graph_count_stations(file_path)
    # Instantiate a StationLineFinder object using the graph
    station_finder = StationLineFinder(london_underground_graph)
    # Create a ShortestPathFinder object with the station finder
    spf = ShortestPathFinder(station_finder)
    # Execute the method to find and print the shortest path
    spf.find_and_print_shortest_path("")
