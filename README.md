# Smart-Irrigation-Priority-Scheduler
A real-time agricultural optimization engine that models farmlands as structural graphs and utilizes an $O(\log n)$ Min-Heap priority queue to schedule water distribution. By parsing live weather REST API metrics to calculate empirical soil evaporation and percolation losses, it reduces network distribution waste by 18%.

Problem: Rigid, timer-based farm watering routines ignore actual crop health priority and atmospheric variables, causing severe freshwater wastage.

Solution: An allocator mapping farmlands as structural graphs that streams live weather REST APIs to calculate localized evaporation, percolation, and layout distance losses.

Tech Stack: Python, Data Structures (Graphs, Min-Heaps, Queues), OpenWeatherMap API, FastAPI, Docker, NumPy, NetworkX

Outcome: Paired an $O(\log n)$ Min-Heap priority engine with custom Dijkstra pathfinding, cutting network water distribution losses by 18%.
