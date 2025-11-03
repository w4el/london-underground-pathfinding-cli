# Import necessary libraries and classes
import pandas as pd
from Graph import Graph_count_stations  # Importing Graph_count_stations class from Graph module
from bellman_ford import bellman_ford  # Import the Bellman-Ford algorithm implementation
import os
# Define a class to find the shortest paths in a graph using Bellman-Ford algorithm
class ShortestPathFinder:
    # Constructor for the class that takes a graph object as an argument
    def __init__(self, graph):
        self.graph = graph  # Store the graph object for later use

    # Method to find shortest paths from all stations to all other stations
    def find_shortest_paths(self):
        all_paths_data = []  # List to store data about all paths
        # Iterate through all source stations in the graph
        for source in self.graph.stations:
            source_index = self.graph.station_to_int[source]  # Get index of the source station
            distances, predecessors, no_negative_cycle = bellman_ford(self.graph.graph, source_index)  # Apply Bellman-Ford algorithm

            # Skip specific stations if needed
            if source in ['station 1', 'station 2']:
                continue

            # Check for negative weight cycles
            if not no_negative_cycle:
                print("A negative-weight cycle detected. Cannot find shortest path.")
                return

            # Iterate through all destination stations
            for destination in self.graph.stations:
                # Skip if destination is not in the desired range or is specific stations
                if destination <= source or destination in ['station 1', 'station 2']:
                    continue
                destination_index = self.graph.station_to_int[destination]  # Get index of the destination station

                # Backtrack the path from destination to source using predecessors
                path = []
                current_station = destination_index
                while predecessors[current_station] is not None:
                    path.insert(0, self.graph.int_to_station[current_station])
                    current_station = predecessors[current_station]
                if current_station == source_index:
                    path.insert(0, source)

                # If a valid path exists, add it to the list
                if path:
                    all_paths_data.append({
                        'Source': source,
                        'Destination': destination,
                        'Path': ' -> '.join(path),
                        'Count of stations': len(path)  # Count the number of stations in the path
                    })

        return all_paths_data  # Return the list of all paths data

    # Method to write the paths data to a CSV file
    def write_paths_to_csv(self, all_paths_data, file_path):
        paths_df = pd.DataFrame(all_paths_data)  # Convert paths data to DataFrame
        paths_df.to_csv(file_path, index=False)  # Save the DataFrame to a CSV file
        print(f"Data saved to {file_path}")  # Print a confirmation message

# Main execution block
if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)    
    # Define the file path for the output CSV file
    csv_file_path = os.path.join(parent_dir, r"Data sets\london_underground_shortest_paths_in_station_count_bellman_ford.csv")
    # Create a graph object using data from the specified Excel file
    london_underground_graph = Graph_count_stations(os.path.join(parent_dir, r"Data sets\London Underground data with times only.xlsx"))
    spf = ShortestPathFinder(london_underground_graph)  # Create a ShortestPathFinder object with the graph
    shortest_paths_data = spf.find_shortest_paths()  # Find the shortest paths
    spf.write_paths_to_csv(shortest_paths_data, csv_file_path)  # Write the paths data to a CSV file
