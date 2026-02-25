class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        visited = set()
        heap = []
        rows = len(heightMap)
        cols = len(heightMap[0])
        res = 0
        # Adding boundary
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows-1 or c == 0 or c == cols - 1:
                    heapq.heappush(heap, (heightMap[r][c], (r, c)))
                    visited.add((r, c))

        def check(h, r, c):
            nonlocal res, rows, cols
            nei = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in nei:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows) and (0 <= nc < cols) and (nr, nc) not in visited:
                    nh = heightMap[nr][nc]
                    if nh < h:
                        res += (h - nh)
                        heapq.heappush(heap, (h, (nr, nc)))
                    else:
                        heapq.heappush(heap, (nh, (nr, nc)))
                    visited.add((nr, nc))

        while heap:
            h, coords = heapq.heappop(heap)
            r, c = coords
            check(h, r, c)

        return res
