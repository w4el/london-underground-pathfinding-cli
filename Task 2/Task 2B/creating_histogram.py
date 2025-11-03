import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
file_path = os.path.join(parent_dir, r"Data sets\london_underground_shortest_paths_in_station_count_dijkstras.csv")
df = pd.read_csv(file_path)
# Extract the travel time data
travel_times = df['Count of stations']
# Define the bins for the histogram so that each bin corresponds to a single minute
single_minute_bins = np.arange(0, travel_times.max() + 1)  # Bins from 0 to the max travel time
# Plot the histogram with individual bins for each minute
plt.figure(figsize=(15, 6))
plt.hist(travel_times, bins=single_minute_bins, color='blue', edgecolor='black', align='left')
plt.title('Histogram of Travel Time (count of stations) before closure - dijkstras')
plt.xlabel('Travel Time (count of stations)')
plt.ylabel('Frequency')
plt.xlim(0, travel_times.max())  # Limit x-axis to max travel time for better visibility
plt.show()

# # Plot the histogram zoomed in around the 40 minute travel time
# plt.figure(figsize=(15, 6))
# plt.hist(travel_times, bins=single_minute_bins, color='blue', edgecolor='black', align='left')
# plt.title('Histogram of Travel Time (minutes) - Zoomed In at 40 Minutes')
# plt.xlabel('Travel Time (minutes)')
# plt.ylabel('Frequency')
# plt.xlim(1,5)  # Zoom in on the 40 minute mark
# plt.show()
