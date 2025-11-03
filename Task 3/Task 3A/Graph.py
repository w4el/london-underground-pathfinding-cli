import pandas as pd
from adjacency_list_graph import AdjacencyListGraph
class Graph_count_stations:
    def __init__(self, file_path):
        # Read our Excel file and store its data in a table (DataFrame).
        self.db = pd.read_excel(file_path, sheet_name='Sheet1')
        
        # Get all unique station names from our data.
        self.stations = pd.concat([self.db['station 1'], self.db['station 2']]).unique()
        
        # Create a dictionary to convert station names to numbers.
        self.station_to_int = {station: i for i, station in enumerate(self.stations)}
        
        # Create a dictionary to convert numbers back to station names.
        self.int_to_station = {i: station for i, station in enumerate(self.stations)}
        
        # Make our graph to store stations and connections between them.
        self.graph = AdjacencyListGraph(len(self.stations), directed=False, weighted=True)
        
        # Make a dictionary to remember which tube line connects two stations.
        self.tube_lines = {}
        
        # Fill our graph with stations and connections.
        self.construct_graph()

    def construct_graph(self):
        for index, row in self.db.iterrows():
            try:
                station_1 = self.station_to_int[row['station 1']]
                station_2 = self.station_to_int[row['station 2']]
                
                # Set edge weight to 1 for each connection
                edge_weight = 1
                
                tube_line = row['tube line']
                
                if not self.graph.has_edge(station_1, station_2):
                    self.graph.insert_edge(station_1, station_2, edge_weight)
                    self.tube_lines[(station_1, station_2)] = tube_line
            except ValueError:
                continue
class Graph_journey_duration:
    def __init__(self, file_path):
        # Read our Excel file and store its data in a table (DataFrame).
        self.db = pd.read_excel(file_path, sheet_name='Sheet1')
        
        # Get all unique station names from our data.
        self.stations = pd.concat([self.db['station 1'], self.db['station 2']]).unique()
        
        # Create a dictionary to convert station names to numbers.
        self.station_to_int = {station: i for i, station in enumerate(self.stations)}
        
        # Create a dictionary to convert numbers back to station names.
        self.int_to_station = {i: station for i, station in enumerate(self.stations)}
        
        # Make our graph to store stations and connections between them.
        self.graph = AdjacencyListGraph(len(self.stations), directed=False, weighted=True)
        
        # Make a dictionary to remember which tube line connects two stations.
        self.tube_lines = {}
        
        # Fill our graph with stations and connections.
        self.construct_graph()

    def construct_graph(self):
        # Look at each row in our data.
        for index, row in self.db.iterrows():
            try:
                # Change station names to numbers.
                station_1 = self.station_to_int[row['station 1']]
                station_2 = self.station_to_int[row['station 2']]
                
                # Change travel time to a number.
                journey_time = float(row['time in minutes between the stations'])
                
                # Remember the name of the tube line for this connection.
                tube_line = row['tube line']
                
                # Add a connection between stations to our graph (if it's not already there).
                if not self.graph.has_edge(station_1, station_2):
                    self.graph.insert_edge(station_1, station_2, journey_time)
                    self.tube_lines[(station_1, station_2)] = tube_line
            except ValueError:
                # If something goes wrong (like if the data is not a number), skip this row.
                continue