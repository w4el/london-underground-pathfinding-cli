# London Underground Pathfinding System

> A Python software solution for pathfinding in the London Underground network. This project's core focus is on the data engineering and analysis code required to apply shortest-path algorithms to a graph built from Pandas DataFrames.

This repository contains the code for a complete system that can:
1.  Load and process complex transit data (stations, connections, journey times).
2.  Construct a graph representation of the network using Pandas.
3.  Apply pathfinding algorithms (Dijkstra's and SSSP) to this data structure.
4.  Analyse the performance of these algorithms using synthetic data.

## 1. Key Features & Technical Implementation

* **Pandas-Based Graph Architecture:** The key engineering decision of this project was to leverage **Pandas** for all data manipulation and graph representation. Instead of native Python objects, DataFrames are used to hold the graph of stations and connections, allowing for efficient loading, querying, and processing.

* **Algorithm Application Scripts (`dijkstras.py`, `single_source_shortest_path.py`):** This project contains the necessary code to *apply* standard shortest-path algorithms to the Pandas-based graph. These scripts are not just the algorithms themselves, but the critical "glue code" that makes them usable on this specific data structure.
    * **`dijkstras.py`:** Applies Dijkstra's algorithm to find the single shortest path between two stations.
    * **`single_source_shortest_path.py`:** Applies the Single Source Shortest Path algorithm to find all optimal routes from one starting station.

* **Empirical Performance Analysis:** The repository includes a comprehensive performance analysis suite. This code **programmatically generates synthetic data** of varying network sizes, runs the pathfinding algorithms on this data, and uses **Matplotlib** to plot the results, demonstrating the scalability and efficiency of the solution.

* **Software Testing:** The solution was developed with a comprehensive testing strategy to ensure the correctness of the data processing and algorithm application.

## 2. Technologies & Libraries Used

* **Core:** Python
* **Data Structure & Manipulation:** Pandas (This is the core of the project)
* **Numerical Analysis:** NumPy
* **Data Visualisation:** Matplotlib (for performance plots)
* **Methodology:** Algorithm Application, Data Modelling, Performance Analysis, Software Testing.

## 3. Installation & Usage

1.  Clone the repository:
    `git clone https://github.com/w4el/london-underground-pathfinder.git`
2.  Navigate to the project directory:
    `cd london-underground-pathfinder`
3.  Install the required dependencies from the `requirements.txt` file:
    `pip install -r requirements.txt`

## 4. How to Use This Project

This project provides the core Python modules for pathfinding and analysis.

The intended workflow is:
1.  Use the data-loading functions to read station and connection `.csv` files into Pandas DataFrames.
2.  Pass these DataFrames to the functions within `dijkstras.py` or `single_source_shortest_path.py` to calculate a route.
3.  The scripts for performance analysis can be run to generate and plot the efficiency of these algorithms on your data.
