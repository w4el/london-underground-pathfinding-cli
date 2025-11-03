# Import necessary libraries and classes
import pandas as pd
import time
import random
from unittest.mock import patch
import os
from Task_3A import ShortestPathFinder, StationLineFinder  # Assuming these classes are defined in Task_3A
from Graph import Graph_journey_duration  # Importing Graph_journey_duration class from Graph module

# Define a class to record performance metrics
class PerformanceRecorder:
    # Initialize the recorder with a directory and optional filename
    def __init__(self, directory, filename='performance_analysis.xlsx'):
        self.records = []  # List to store performance records
        self.directory = directory  # Directory to save the file
        self.filename = filename  # Filename for the Excel file

    # Method to add a performance record
    def add_record(self, num_lines, num_stations_per_line, time_taken):
        # Append performance data to the records list
        self.records.append({
            'Number of Lines': num_lines,
            'Stations per Line': num_stations_per_line,
            'Total Number of Stations': num_lines * num_stations_per_line,
            'Time Taken (s)': time_taken
        })

    # Method to save records to an Excel file
    def save_to_excel(self):
        df = pd.DataFrame(self.records)  # Convert records list to DataFrame
        summary = df.describe()  # Generate summary statistics
        filepath = os.path.join(self.directory, self.filename)  # Full filepath for the Excel file
        
        # Write data and summary to Excel with charts
        with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Raw Data', index=False)
            summary.to_excel(writer, sheet_name='Summary', index=True)

            # Create and insert a line chart in the Excel file
            workbook = writer.book
            worksheet = writer.sheets['Raw Data']
            chart = workbook.add_chart({'type': 'line'})
            chart.add_series({
                'name': '=Raw Data!$D$1',
                'categories': '=Raw Data!$C$2:$C${}'.format(len(self.records) + 1),
                'values': '=Raw Data!$D$2:$D${}'.format(len(self.records) + 1),
            })
            worksheet.insert_chart('F2', chart)

    # Static method to generate synthetic data for testing
    @staticmethod
    def generate_synthetic_data(num_lines, num_stations_per_line, num_interchange_stations):
        # Creating synthetic data for tube lines and stations
        tube_lines = [f'Line_{i}' for i in range(1, num_lines + 1)]
        data = []
        interchange_stations_dict = {}

        # Generate station data for each tube line
        for line in tube_lines:
            stations = [f'Station_{line}_{i}' for i in range(1, num_stations_per_line + 1)]
            for i in range(num_stations_per_line - 1):
                data.append({
                    'tube line': line,
                    'station 1': stations[i],
                    'station 2': stations[i + 1],
                    'time in minutes between the stations': str(2)  # Assuming a fixed time between stations
                })
            # Randomly select interchange stations
            interchange_stations = random.sample(stations, min(num_interchange_stations, num_stations_per_line))
            interchange_stations_dict[line] = interchange_stations

        # Generate data for interchange connections
        for i, line in enumerate(tube_lines):
            for j in range(num_interchange_stations):
                if i + j < num_lines - 1:
                    next_line = tube_lines[(i + j + 1) % num_lines]
                    current_interchange_station = interchange_stations_dict[line][j]
                    next_interchange_station = interchange_stations_dict[next_line][j]
                    data.append({
                        'tube line': f'Interchange {line}-{next_line}',
                        'station 1': current_interchange_station,
                        'station 2': next_interchange_station,
                        'time in minutes between the stations': str(2)
                    })

        return pd.DataFrame(data)

# Static method to analyze the performance of the shortest path algorithm
@staticmethod
def analyze_performance(num_lines, num_stations_per_line, num_interchange_stations, line, directory):
    # Generate synthetic data and save it to an Excel file
    df = PerformanceRecorder.generate_synthetic_data(num_lines, num_stations_per_line, num_interchange_stations)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
  
    # Save the synthetic data to an Excel file
    file_path = os.path.join(directory, 'synthetic_data_stations_count_bellman_ford.xlsx')
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as excel_buffer:
        df.to_excel(excel_buffer, sheet_name='Sheet1', index=False)
    
    # Create a graph and initialize the shortest path finder
    graph = Graph_journey_duration(file_path)
    station_finder = StationLineFinder(graph)
    spf = ShortestPathFinder(station_finder)
    
    # Randomly choose start and end stations for the shortest path
    line_stations = [station for station in graph.stations if f'Line_{line}' in station]
    start_station = random.choice(line_stations)
    end_station = random.choice(graph.stations)

    # Mock user inputs for start and end stations
    user_input = [start_station, end_station]
    with patch('builtins.input', side_effect=lambda prompt: user_input.pop(0)):
        # Measure the time taken to find and print the shortest path
        start_time = time.perf_counter()
        spf.find_and_print_shortest_path(line)  
        end_time = time.perf_counter()

    # Calculate and return the time taken
    time_taken = end_time - start_time
    return time_taken

# Main execution block
if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    # Define parameters for performance analysis
    num_lines = 15 
    num_interchange_stations = 1  
    directory = os.path.join(parent_dir, r"Data sets")
    performance_results = []

    # Analyze performance for different numbers of stations
    for num_stations in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500 ,550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3650, 3700, 3750, 3800, 3850, 3900, 3950, 4000, 4050, 4100, 4150, 4200, 4250, 4300, 4350, 4400, 4450, 4500, 4550, 4600, 4650, 4700, 4750, 4800, 4850, 4900, 4950, 5000]:
        num_stations_per_line = num_stations // num_lines
        for line in range(1, num_lines + 1):
            # Measure the time taken for each case and record it
            time_taken = analyze_performance(num_lines, num_stations_per_line, num_interchange_stations, line, directory)
            performance_results.append({
                'Total Number of Stations': num_stations,
                'Time Taken (s)': time_taken
            })

    # Compile the results into a DataFrame and summarize
    df = pd.DataFrame(performance_results)
    summary_df = df.groupby('Total Number of Stations')['Time Taken (s)'].agg(['mean', 'std', 'min', 'max']).reset_index()

    # Save the results and the summary to an Excel file
    with pd.ExcelWriter(os.path.join(directory, 'performance_analysis.xlsx'), engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Detailed Data', index=False)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        # Create a chart in the Excel file to visualize the performance analysis
        chart = writer.book.add_chart({'type': 'line'})
        chart.add_series({
            'name': 'Average Time Taken',
            'categories': '=Summary!$A$2:$A${}'.format(len(summary_df) + 1),
            'values': '=Summary!$B$2:$B${}'.format(len(summary_df) + 1),
        })
        
        # Set chart properties
        chart.set_x_axis({'name': 'Total Number of Stations'})
        chart.set_y_axis({'name': 'Time Taken (s)', 'major_gridlines': {'visible': True}})
        chart.set_title({'name': 'Performance Analysis'})
        
        # Insert the chart into the Excel summary sheet
        summary_worksheet = writer.sheets['Summary']
        summary_worksheet.insert_chart('F2', chart)
