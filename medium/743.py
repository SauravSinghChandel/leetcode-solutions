class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)

        for u, v, w in times:
            g[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            t = max(t, weight)

            for nei, wei in g[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (weight + wei, nei))

        if len(visited) == n:
            return t
        else:
            return -1
