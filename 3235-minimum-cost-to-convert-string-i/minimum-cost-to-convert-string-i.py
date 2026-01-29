class Solution:
    def minimumCost(self, source: str, target: str, original, changed, cost) -> int:
        INF = 10**18
        n = 26
        
        # Step 1: init distance matrix
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: fill direct edges
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Step 3: Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 4: compute answer
        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]
        
        return ans
