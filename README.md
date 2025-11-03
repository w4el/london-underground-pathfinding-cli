Here is the `README.md` file, structured to match your project's tasks and including all associated graphs and screenshots from the provided document.

-----

# London Underground Route Planner & Network Analyst

This is a personal project designed to model, analyse, and query the London Underground network. The system provides functionalities for finding optimal routes based on different metrics (travel time and station count) and includes a tool for analysing network resilience by simulating line closures.

The implementation uses foundational algorithms and optimised data structures to ensure efficiency and scalability, even with large, complex transit networks.

## Project Structure

The repository is organised by task, with each folder containing the code and analysis for that specific part of the project:

  * **/task1/**: Finds the shortest path based on **travel time (minutes)**.
  * **/task2/**: Finds the shortest path based on **station count (fewest stops)**.
  * **/task3/**: Implements an **alternative algorithm (Bellman-Ford)** for the station count problem.
  * **/task4/**: Analyses network resilience to **line closures** using a Minimum Spanning Tree (MST).

-----

## Task 1: Shortest Path by Travel Time

### Task 1A: Algorithm & Implementation

  * **Objective:** To find the fastest route between any two stations, minimising total journey duration in minutes .
  * **Algorithm:** **Dijkstra's Algorithm** (`dijkstras.py`) .
      * **Rationale:** Chosen for its proven efficacy in finding the shortest path in weighted graphs . It is preferable to Bellman-Ford in this scenario because the network does not have negative weight cycles (negative travel times), and Dijkstra's has a lower time complexity .
  * **Core Data Structures:**
      * **Pandas:** Used for initial data loading and manipulation due to its efficient DataFrame functionality .
      * **Adjacency List Graph** (`Graph.py`): This structure was chosen over an adjacency matrix as the Tube network is sparse . This is far more space-efficient than an $O(V^2)$ matrix .
      * **Min-Heap Priority Queue** (`min_heap_priority_queue.py`, `heap.py`): Essential for an efficient Dijkstra's implementation . It allows for $O(\log n)$ time complexity for insertions and deletions , which is far superior to the $O(n)$ of a simple array .
      * **Doubly Linked List (DLL) with Sentinel** (`dll_sentinel.py`): Used to implement the adjacency lists . DLLs provide constant-time $O(1)$ insertions and deletions of edges . The sentinel node simplifies the code by removing the need for special boundary checks .

**Code Implementation:**

```python
# Imports for Task 1
from Graph import Graph_journey_duration
from dijkstra import dijkstra
import os
```

```python
# Core data structure imports
import pandas as pd
from adjacency_list_graph import AdjacencyListGraph
```

### Task 1B: Performance & Results

  * **Empirical Performance Analysis:**

      * The algorithm's performance was tested using synthetic data ranging from 50 to 5,000 stations .
      * The analysis shows a near-linear increase in average time as the number of stations grows, aligning with its $O(V \log V + E)$ complexity . This confirms the solution is efficient and scalable for a responsive transit application .

  * **Histogram Analysis:**

      * The histogram of travel times for all possible station pairs shows a **right-skewed distribution** .
      * Most journeys are relatively quick, with a peak frequency between 20-40 minutes .
      * The long tail to the right indicates that a smaller number of journeys are significantly longer, likely those traversing large distances or requiring multiple line changes .

  * **Functionality & Test Results:**

      * The application correctly calculates the shortest path and total time, providing clear, turn-by-turn directions, including line switches .
      * All test cases produced the correct routes and durations, and error handling for non-existent stations was successful .

| Test Case | Test data | Expected outcome | Actual outcome | Correctness | notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Directly Connected Stations** | Bank-waterloo | 5 mins | 5 mins | pass | It chooses the shortest path despite the station existing in other lines |
| **Long-Distance Station Pairs** | Epping-Amersham | 100 mins | 100 mins | pass | There was a lot of switches and stations but it was efficient and quick in finding the correct shortest path |
| **Short-Distance Station Pairs** | Waterloo – South Kenton | 35 mins | 35 mins | pass | Despite a path existing on one line the algorithm a path that needs switching but it took shorter time which is the whole requirement |
| **Error handling** | Bnak instead of Bank | Station not found. Please check the name and try again. | Station not found. Please check the name and try again. | pass | It prompts the use to enter station again without needing to re-launch the code |
-----

## Task 2: Shortest Path by Station Count

### Task 2A: Algorithm & Implementation

  * **Objective:** To find the route with the fewest stops between any two stations, regardless of travel time .
  * **Algorithm:** **Dijkstra's Algorithm** (`dijkstras.py`) .
      * **Rationale:** The same algorithm from Task 1 was adapted for this problem. By treating the graph as "unweighted," (i.e., assigning a uniform weight of **'1'** to every edge/connection), Dijkstra's algorithm inherently finds the path with the fewest edges, which in this case corresponds to the fewest stations .
  * **Core Data Structures:** This task uses the same data structures as Task 1 (Pandas, Adjacency List, Min-Heap) .

**Code Implementation:**

```python
# Imports for Task 2
from Graph import Graph_count_stations # Assuming this class is defined in the Graph module.
from dijkstra import dijkstra # Import the Dijkstra's algorithm implementation.
import os
```

```python
# Run Dijkstra's algorithm to find the shortest path and its distance.
distances, predecessors = dijkstra(self.station_finder.graph.graph, source_index)
```

### Task 2B: Performance & Results

  * **Empirical Performance Analysis:**

      * As in Task 1, the performance analysis using synthetic data (50 to 5,000 stations) confirmed a consistent, near-linear escalation in processing time .
      * This result is in line with the $O(V \log V + E)$ complexity and validates the algorithm's efficiency for this metric as well .

  * **Histogram Analysis:**

      * The histogram for journey times measured by station count displays a **right-skewed distribution** (described as such in the text , though the graph appears more normal).
      * The peak frequency is for journeys of around 10-15 stations, indicating that most trips in the network involve this many stops .

  * **Functionality & Test Results:**

      * The application successfully charts the path with the minimum number of stations .
      * Tests confirmed that the algorithm correctly identifies the path with the fewest stops .
      * All test cases, including long-distance, short-distance, and error handling, passed successfully .

| Test Case | Test data | Expected outcome | Actual outcome | Correctness | notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Directly Connected Stations** | Bank-waterloo | 2 | 2 | pass | It chooses the shortest path despite the station existing in other lines |
| **Long-Distance Station Pairs** | Epping-Amersham | 31 | 31 | pass | There was a lot of switches and stations but it was efficient and quick in finding the correct shortest path |
| **Short-Distance Station Pairs** | Bank – Canary wharf | 5 | 5 | pass | The algorithm ignored the direct path on one lline as it is not shortest |
| **Error handling** | Bnak instead of Bank | Station not found. Please check the name and try again. | Station not found. Please check the name and try again. | pass | It prompts the use to enter station again without needing to re-launch the code |

-----

## Task 3: Alternative Shortest Path (Bellman-Ford)

### Task 3A: Algorithm & Implementation

  * **Objective:** To solve the station count problem (Task 2) using an alternative algorithm for comparison and robustness testing .

  * **Algorithm:** **Bellman-Ford Algorithm** (`bellman_ford.py`) .

      * **Rationale:** Bellman-Ford was selected for its ability to handle negative weights, providing robustness against such scenarios (e.g., in future fare strategy changes) . It was chosen over other all-pairs algorithms like Floyd-Warshall due to its suitability for single-source problems and lower $O(VE)$ complexity compared to Floyd-Warshall's $O(V^3)$ .

  * **Performance:**

      * The algorithm's theoretical complexity is $O(VE)$ .
      * This was confirmed by the empirical analysis, which showed a much more pronounced, non-linear growth in computation time . This test confirms that while functional, Bellman-Ford is computationally more expensive for this problem than Dijkstra's .

**Code Implementation:**

```python
# Imports for Task 3
from Graph import Graph_count_stations # Importing Graph_count_stations class from Graph module
from bellman_ford import bellman_ford # Import the Bellman-Ford algorithm implementation
import os
```

```python
# Run Bellman-Ford algorithm to find the shortest path and its distance
distances, predecessors, no_negative_cycle = bellman_ford(self.station_finder.graph.graph, source_index)
```

### Task 3B: Performance & Results

  * **Histogram Analysis:**

      * The histogram of journey lengths (station counts) mirrors the one from Task 2B . This is expected, as both algorithms find the correct shortest path; Bellman-Ford simply takes longer to do so .

  * **Test Results:**

      * The test table is identical to Task 2, confirming the algorithm's **correctness** (it finds the right answer) even if it is less **efficient** .

| Test Case | Test data | Expected outcome | Actual outcome | Correctness | notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Directly Connected Stations** | Bank-waterloo | 2 | 2 | pass | It chooses the shortest path despite the station existing in other lines |
| **Long-Distance Station Pairs** | Epping-Amersham | 31 | 31 | pass | There was a lot of switches and stations but it was efficient and quick in finding the correct shortest path |
| **Short-Distance Station Pairs** | Bank – Canary wharf | 5 | 5 | pass | The algorithm ignored the direct path on one lline as it is not shortest |
| **Error handling** | Bnak instead of Bank | Station not found. Please check the name and try again. | Station not found. Please check the name and try again. | pass | It prompts the use to enter station again without needing to re-launch the code |

-----

## Task 4: Network Resilience & Closure Analysis

### Task 4A: Algorithm & Implementation (MST)

  * **Objective:** To analyse the impact of potential line closures by identifying redundant connections. The system determines which connections can be removed while ensuring that travel between any two stations remains possible .
  * **Algorithm:** **Kruskal's Algorithm** (`mst.py`) .
      * **Rationale:** Kruskal's algorithm was chosen to build a Minimum Spanning Tree (MST) for its simplicity and efficiency, especially in sparse graphs like a transport network . An MST connects all stations using the minimum possible total weight. By finding the MST, I can identify all "essential" connections. Any edge **not** in the MST is redundant and can be removed without disconnecting the network.
  * **Supporting Algorithms & Data Structures:**
      * **Merge Sort** (`merge_sort.py`): Kruskal's requires sorting all graph edges by weight. Merge Sort was chosen for its stable sorting behaviour and guaranteed $O(n \log n)$ worst-case performance .
      * **Disjoint Set Forest** (`disjoint_set_forest.py`): This data structure is essential for Kruskal's algorithm . It provides a highly efficient (nearly constant time) `union-find` operation, which is used to detect cycles as edges are added to the MST .

**Code Implementation:**

```python
# Imports for Task 4
from Graph import Graph_journey_duration # Importing Graph_journey_duration class from Graph module
from mst import kruskal # Import the Kruskal's algorithm for minimum spanning tree
import os
```

```python
# Apply Kruskal's algorithm to find the minimum spanning tree
mst = kruskal(self.graph.graph)
```

### Task 4B: Performance & Impact Analysis

  * **Empirical Performance Analysis (Kruskal's):**

      * Performance was measured using both time and total operation count on synthetic data up to 5000 stations .
      * The analysis showed that while execution time fluctuated, the number of operations scaled linearly . This suggests the $O(E)$ edge iteration was the dominant factor, confirming the algorithm's high efficiency and scalability for this task .

Operations vs. Stations

<img width="350" height="211" alt="image" src="https://github.com/user-attachments/assets/9b05ea7e-15a9-4567-a86e-98aafbb91cd7" />

Time vs. Stations

<img width="358" height="211" alt="image" src="https://github.com/user-attachments/assets/15a029ad-7738-43b1-ae2c-34ba4720c263" />




  * **Functionality & Results (Closure Analysis):**

      * The application successfully generates a list of connections that can be removed while maintaining full network connectivity . This was validated by running an all-pairs shortest path check after the simulated removals, which confirmed that no stations were isolated .
      * The screenshots below show the lists of removable connections, calculated based on both station count and travel duration.

<img width="1500" height="600" alt="duration before closure dijkstras" src="https://github.com/user-attachments/assets/49e7fc0a-481b-48a5-8448-fc7a17d2a0c9" />
<img width="1500" height="600" alt="duration after closure" src="https://github.com/user-attachments/assets/0d557a49-bf4e-4702-93f2-c761fc865fe8" />
<img width="1500" height="600" alt="count before closure dijkstras" src="https://github.com/user-attachments/assets/da5308c4-dff2-475c-928f-e07c23c66c8f" />
<img width="1500" height="600" alt="count before closure bellman_ford" src="https://github.com/user-attachments/assets/82fef8cd-3614-4977-81de-d67b5224f350" />
<img width="1500" height="600" alt="count afer closure" src="https://github.com/user-attachments/assets/3d044e8f-0220-4480-8671-f9920e24d1ab" />


-----

## Final Remarks & Limitations

This project successfully demonstrates the application of fundamental graph algorithms to a real-world transportation network. The implementations of Dijkstra's, Bellman-Ford, and Kruskal's algorithms, along with appropriate data structures like adjacency lists and priority queues, provided an effective solution for route planning and network analysis .

Key limitations and areas for future work include:

1.  **Static Data:** The system's accuracy is entirely dependent on the input dataset . It does not account for real-time, dynamic factors like service disruptions, delays, or time-of-day variations in travel time .
2.  **User Interface:** The current implementation is a command-line tool. A significant improvement would be a graphical user interface (GUI) to provide a more intuitive and interactive user experience .
3.  **Data Completeness:** The project noted minor issues with data consistency (e.g., stations with slight name variations due to whitespace) which had to be handled . A more robust data-cleaning pipeline would be beneficial.
4.  **Real-World Testing:** The application was validated against synthetic data and known routes . Extensive real-world testing with actual commuters would be a valuable next step to gather feedback and refine functionality .

## References

  * Cormen, T.H., Leiserson, C.E., Rivest, R.L. and Stein, C., 2009. “Introduction to Algorithms”, 3rd ed. MIT Press.
  * Fredman, M.L. and Tarjan, R.E., 1987. Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms. “Journal of the ACM”, 34(3), pp.596-615.
  * Galil, Z. and Italiano, G.F., 1991. Data Structures and Algorithms for Disjoint Set Union Problems. “ACM Computing Surveys”, 23(3), pp.319-344.
  * Knuth, D.E., 1997. “The Art of Computer Programming, Volume 1: Fundamental Algorithms”, 3rd ed. Addison-Wesley.
  * McKinney, W., 2010. Data Structures for Statistical Computing in Python. In: “Proceedings of the 9th Python in Science Conference”.
  * Sedgewick, R., 1998. “Algorithms in C++, Parts 1-4: Fundamentals, Data Structure, Sorting, Searching”, 3rd ed. Addison-Wesley.
  * Skiena, S.S., 2008. “The Algorithm Design Manual”, 2nd ed. Springer.
  * Tarjan, R.E., 1983. *Data Structures and Network Algorithms*. SIAM.
  * Williams, J.W.J., 1964. Algorithm 232: Heapsort. “Communications of the ACM”, 7(6), pp.347-348.
  * Bondy, J.A. and Murty, U.S.R., 1976. “Graph Theory with Applications”. North-Holland.
  * Even, S., 2011. “Graph Algorithms, 2nd ed.” Cambridge University Press.

<!-- end list -->

```
```
P.S: task 4 was uploaded as a zip due to the amount of files
