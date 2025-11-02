# London Underground Route Planner & Network Analyser

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

This is a Python-based route planning tool for the London Underground network. I built this project to implement, compare, and analyse the performance of fundamental graph algorithms for solving real-world network problems.

The tool can find the optimal path between any two stations based on two different metrics:
1.  **Shortest travel time (minutes)**
2.  **Fewest number of stations**

It also includes a network resilience module to analyse the impact of line closures.

## 🚀 Key Features

* **Fastest Route (by Time):** Implements **Dijkstra's algorithm** on a weighted graph where edge weights represent the travel time in minutes between stations.
* **Fewest Stops Route:** Calculates the path with the minimum number of station-to-station hops. This is implemented using two different algorithms for comparison:
    * **Dijkstra's Algorithm** on an unweighted graph (or with a uniform weight of '1' for each edge).
    * **Bellman-Ford Algorithm**, which is also capable of detecting negative weight cycles (though none exist in this dataset).
* **Network Resilience Analysis:** Uses **Kruskal's algorithm** to find a Minimum Spanning Tree (MST) of the entire network. This is used to identify redundant connections that could be removed (e.g., for maintenance) whilst guaranteeing that all stations remain connected to the network.

## 📊 Core Algorithms & Data Structures

This project was an exercise in implementing these concepts from the ground up.

* **Algorithms:**
    * Dijkstra's (`dijkstras.py`)
    * Bellman-Ford (`bellman_ford.py`)
    * Kruskal's (`mst.py`)
    * Merge Sort (`merge_sort.py`)
* **Data Structures:**
    * **Adjacency List** (`adjacency_list_graph.py`): The primary graph representation, chosen for its space efficiency in a sparse network like a transit system.
    * **Doubly Linked List w/ Sentinel** (`dll_sentinel.py`): Used to implement the adjacency list for efficient $O(1)$ edge insertions/deletions.
    * **Min-Heap Priority Queue** (`min_heap_priority_queue.py`): A crucial component for the efficiency of Dijkstra's algorithm.
    * **Disjoint Set Forest** (`disjoint_set_forest.py`): Used for the efficient union-find operations required by Kruskal's algorithm.
    * **Pandas DataFrame:** Used for initial loading and manipulation of the station data.

## 📦 Project Structure

london-underground-network-analysis/│├── data/│   └── london_underground_dataset.csv  (or similar data file)│├── src/│   ├── algorithms/│   │   ├── dijkstras.py│   │   ├── bellman_ford.py│   │   ├── mst.py│   │   ├── merge_sort.py│   ││   └── data_structures/│       ├── Graph.py│       ├── adjacency_list_graph.py│       ├── dll_sentinel.py│       ├── min_heap_priority_queue.py│       ├── disjoint_set_forest.py│├── notebooks/│   └── performance_analysis.ipynb│├── main.py                         # Main script to run the application├── requirements.txt                # Project dependencies├── .gitignore├── https://www.google.com/search?q=LICENSE└── README.md
## ⚙️ Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/w4el/london-underground-network-analysis.git](https://github.com/w4el/london-underground-network-analysis.git)
    cd london-underground-network-analysis
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Usage

The application is run from the command line.

### Find Fastest Route (by Time)

```bash
python main.py --type time --start "Epping" --end "Amersham"
Example Output:Shortest path: Go in Central Line in Epping -> ... [Switch to Metropolitan Line at Baker Street] ... -> Amersham
Total travel time: 100.0 minutes
Find Fewest StopsBashpython main.py --type stations --start "Bank" --end "Waterloo"
Example Output:Shortest path (by number of stations): Bank -> ... -> Waterloo
Total stations in the path: 2 stations
Run Closure AnalysisBashpython main.py --analyse-closures
Example Output:Analysis of potential tube line closures:
Circle line can have the following connections removed:
- Baker Street
- Euston Square
...
Metropolitan line can have the following connections removed:
- Baker Street
- Finchley Road
...
All stations remain connected.
📈 Performance FindingsDijkstra's algorithm demonstrated a near-linear increase in time as the number of stations grew, aligning with its $O(V \log V + E)$ complexity and confirming its suitability for a responsive application.Bellman-Ford's algorithm showed a more pronounced quadratic growth in computation time, consistent with its $O(V \times E)$ complexity.
