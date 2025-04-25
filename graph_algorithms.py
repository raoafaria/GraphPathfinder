import sys
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

def bellman_ford(graph, vertices, start):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0

    for _ in range(len(vertices) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in graph:
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                return "Graph contains a negative-weight cycle"

    return dist

def floyd_warshall(graph, vertices):
    # In-place update: only O(n^2) space used
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}
    for v in vertices:
        dist[v][v] = 0

    for u in graph:
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in vertices:
        for i in vertices:
            for j in vertices:
                # In-place update to minimize space complexity
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def example_graph():
    return {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 3, 'D': 2, 'E': 3},
        'C': {'B': 1, 'D': 4, 'E': 5},
        'D': {},
        'E': {'D': 1}
    }, ['A', 'B', 'C', 'D', 'E']

def print_distances(dist):
    if isinstance(dist, str):
        print(dist)
    elif isinstance(dist, dict) and isinstance(next(iter(dist.values())), dict):
        for u in dist:
            for v in dist[u]:
                print(f"{u} -> {v}: {dist[u][v]}")
            print()
    else:
        for node in dist:
            print(f"Distance to {node}: {dist[node]}")

def main():
    graph, vertices = example_graph()
    while True:
        print("\n===== Graph Algorithm Menu =====")
        print("1. Run Dijkstra's Algorithm")
        print("2. Run Bellman-Ford Algorithm")
        print("3. Run Floyd-Warshall Algorithm")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            start = input(f"Enter start node from {vertices}: ")
            if start in vertices:
                print("Note: Dijkstra's Algorithm assumes no negative-weight edges.")
                dist = dijkstra(graph, start)
                print_distances(dist)
            else:
                print("Invalid start node.")
        elif choice == '2':
            start = input(f"Enter start node from {vertices}: ")
            if start in vertices:
                dist = bellman_ford(graph, vertices, start)
                print_distances(dist)
            else:
                print("Invalid start node.")
        elif choice == '3':
            dist = floyd_warshall(graph, vertices)
            print_distances(dist)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
