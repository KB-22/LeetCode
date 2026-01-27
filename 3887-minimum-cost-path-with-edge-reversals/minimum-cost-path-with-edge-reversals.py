import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        out_edges = defaultdict(list)
        in_edges = defaultdict(list)

        for u, v, w in edges:
            out_edges[u].append((v, w))
            in_edges[v].append((u, w))  # incoming edges

        INF = 10**18
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]  # (cost, node, used_switch)

        while pq:
            cost, u, used = heapq.heappop(pq)

            if cost > dist[u][used]:
                continue

            # 1️⃣ Normal outgoing edges
            for v, w in out_edges[u]:
                if cost + w < dist[v][0]:
                    dist[v][0] = cost + w
                    heapq.heappush(pq, (cost + w, v, 0))

            # 2️⃣ Reverse incoming edges (only once per node)
            if used == 0:
                for v, w in in_edges[u]:
                    new_cost = cost + 2 * w
                    if new_cost < dist[v][0]:
                        dist[v][0] = new_cost
                        heapq.heappush(pq, (new_cost, v, 0))

        ans = min(dist[n - 1])
        return -1 if ans == INF else ans
