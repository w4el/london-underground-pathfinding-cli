# Import necessary classes and modules
from Graph import Graph_journey_duration, pd  # Assuming Graph_journey_duration class and pandas are defined in Graph module.
from dijkstra import dijkstra  # Importing dijkstra algorithm implementation.
import os
# Define a class for finding the shortest paths in a graph.
class ShortestPathFinder:
    # Initializer for the class, takes a graph object as an argument.
    def __init__(self, graph):
        self.graph = graph  # Store the graph object for use in other methods.

    # Method to find the shortest paths from all stations to all other stations.
    def find_shortest_paths(self):
        all_paths_data = []  # List to store data about all paths.
        for source in self.graph.stations:  # Iterate through all source stations.
            source_index = self.graph.station_to_int[source]  # Convert station name to index.
            distances, predecessors = dijkstra(self.graph.graph, source_index)  # Run Dijkstra's algorithm.

            # Skip specific stations as per the condition.
            if source == 'station 1' or source == 'station 2':
                continue

            # Iterate through all destination stations.
            for destination in self.graph.stations:
                # Skip if the destination is not in the desired range or is specific stations.
                if destination <= source or destination in ['station 1', 'station 2']:
                    continue
                destination_index = self.graph.station_to_int[destination]  # Convert station name to index.

                # Backtrack the path from destination to source using predecessors.
                path = []
                current_station = destination_index
                while predecessors[current_station] is not None:
                    path.insert(0, self.graph.int_to_station[current_station])
                    current_station = predecessors[current_station]
                if current_station == source_index:
                    path.insert(0, source)

                # If a valid path exists, add it to the list.
                if path:
                    all_paths_data.append({
                        'Source': source,
                        'Destination': destination,
                        'Path': ' -> '.join(path),
                        'Travel Time (minutes)': distances[destination_index]
                    })

        return all_paths_data  # Return the list of all paths data.

    # Method to write the paths data to a CSV file.
    def write_paths_to_csv(self, all_paths_data, file_path):
        # Convert the paths data to a DataFrame.
        paths_df = pd.DataFrame(all_paths_data)
        paths_df.to_csv(file_path, index=False)  # Save the DataFrame to a CSV file.
        print(f"Data saved to {file_path}")  # Print a confirmation message.

# Main execution block.
if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    # Define the file path for the output CSV file.
    csv_file_path = os.path.join(parent_dir, r"Data sets\london_underground_shortest_paths_in_journey_duration.csv")
    # Create a graph object using data from the specified Excel file.
    london_underground_graph = Graph_journey_duration(os.path.join(parent_dir, r"Data sets\London Underground data with times only.xlsx"))
    spf = ShortestPathFinder(london_underground_graph)  # Create a ShortestPathFinder object with the graph.
    shortest_paths_data = spf.find_shortest_paths()  # Find the shortest paths.
    spf.write_paths_to_csv(shortest_paths_data, csv_file_path)  # Write the paths data to a CSV file.
