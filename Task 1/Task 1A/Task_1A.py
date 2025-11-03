# Import the necessary modules for handling the graph and Dijkstra's algorithm.
from Graph import Graph_journey_duration
from dijkstra import dijkstra
import os
# Define a class to handle finding stations and tube lines on the London Underground graph.
class StationLineFinder:
    # Initializer for the class, takes a graph as an argument.
    def __init__(self, graph):
        self.graph = graph  # Store the graph object for later use.

    # Method to find the full name of a station given a partial or case-insensitive name.
    def find_station_name(self, station_name):
        # Iterate over all stations in the graph.
        for real_name in self.graph.stations:
            # Check if the provided station name matches (ignoring case) with any real station name.
            if station_name.lower() == real_name.lower():
                return real_name  # Return the matching real station name.
        return None  # If no match is found, return None.

    # Method to get the index of a station from the user input.
    def get_station_index(self, station_name_prompt):
        while True:  # Keep looping until a valid station is found.
            station_name = input(station_name_prompt).strip().title()  # Get user input and format it.
            matched_station = self.find_station_name(station_name)  # Find the full station name.
            if matched_station:
                # If a matching station is found, return its index from the graph.
                return self.graph.station_to_int[matched_station]
            print("Station not found. Please check the name and try again.")  # Error message if not found.

    # Method to get the tube line connecting two stations.
    def get_tube_line(self, station1, station2):
        # Check the tube_lines dictionary for a direct or reverse tuple of the stations.
        return self.graph.tube_lines.get((station1, station2)) or self.graph.tube_lines.get((station2, station1))

# Define a class for finding the shortest path between two stations.
class ShortestPathFinder():
    # Initializer for the class, takes a StationLineFinder object as an argument.
    def __init__(self, station_finder):
        self.station_finder = station_finder  # Store the station finder object for later use.

    # Method to find and print the shortest path between two stations.
    def find_and_print_shortest_path(self, line):
        # Get the index of the source and destination stations from user input.
        source_index = self.station_finder.get_station_index("Enter the start station: ")
        destination_index = self.station_finder.get_station_index("Enter the destination station: ")

        # Run Dijkstra's algorithm on the graph to find the shortest path.
        distances, predecessors = dijkstra(self.station_finder.graph.graph, source_index)

        # Initialize a path list starting from the destination station.
        path = [self.station_finder.graph.int_to_station[destination_index]]
        current_station = destination_index  # Start from the destination station.
        previous_line = None  # Initialize the previous line as None.

        # Loop to backtrack the path from the destination to the source.
        while predecessors[current_station] is not None:
            next_station = predecessors[current_station]  # Get the next station in the path.
            line = self.station_finder.get_tube_line(next_station, current_station)  # Get the tube line for this path segment.

            # If there is a line change, add a message to the path list.
            if previous_line is not None and line != previous_line:
                path.insert(1, f"(Switch to {previous_line} line at {self.station_finder.graph.int_to_station[current_station]})")

            current_station = next_station  # Update the current station.
            path.insert(0, self.station_finder.graph.int_to_station[current_station])  # Add the current station to the path.
            previous_line = line  # Update the previous line.

        # Print the shortest path and total travel time.
        print("Shortest path:", "Go on", line, "line in", self.station_finder.graph.int_to_station[source_index], "-->", " -> ".join(path))
        print(f"Total travel time: {distances[destination_index]} minutes")

# Main execution block.
if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    # Define the file path for the London Underground data set.
    file_path = os.path.join(parent_dir, r"Data sets\London Underground data with times only.xlsx")
    # Create a graph object for the London Underground.
    london_underground_graph = Graph_journey_duration(file_path)
    # Create a StationLineFinder object using the graph.
    station_finder = StationLineFinder(london_underground_graph)
    # Create a ShortestPathFinder object using the station finder.
    spf = ShortestPathFinder(station_finder)

    # Call the method to find and print the shortest path.
    spf.find_and_print_shortest_path("")
