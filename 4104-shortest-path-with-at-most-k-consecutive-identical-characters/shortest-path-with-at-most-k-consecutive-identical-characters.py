
import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:

        # Step 1: Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # Step 2: Initialize distance array
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Starting node has 1 consecutive character
        dist[0][1] = 0

        # Heap: (cost, node, consecutive_count)
        heap = [(0, 0, 1)]

        # Step 3: Dijkstra's algorithm
        while heap:
            cost, u, count = heapq.heappop(heap)

            # Skip outdated states
            if cost > dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return cost

            # Explore outgoing edges
            for v, weight in graph[u]:

                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1

                # Reject invalid consecutive sequences
                if next_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[v][next_count]:
                    dist[v][next_count] = new_cost

                    heapq.heappush(
                        heap,
                        (new_cost, v, next_count)
                    )

        return -1
