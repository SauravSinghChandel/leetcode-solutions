class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        visited = set()
        minHeap = [[0, 0]]
        
        cost = 0

        while len(visited) < n:
            weight, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            cost += weight
            visited.add(node)

            for neiWeight, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiWeight, nei])

        return cost
