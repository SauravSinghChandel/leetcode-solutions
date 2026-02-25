class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        adj = [[] for i in range(n)]

        for u, v, d in flights:
            adj[u].append([v, d])

        q = deque([(0, src, 0)])

        while q:
            cost, node, stops = q.popleft()

            if stops > k:
                continue

            for nei, neiCost in adj[node]:
                nextCost = cost + neiCost

                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return -1 if prices[dst] == float('inf') else prices[dst]
