class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]

        heap = [(grid[0][0], 0, 0)]

        dirs = [(1, 0), (-1 , 0), (0, 1), (0, -1)]

        while heap:
            height, r, c = heapq.heappop(heap)
            if r == c == n - 1:
                return height

            if visited[r][c]:
                continue

            visited[r][c] = True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_height = max(height, grid[nr][nc])
                    heapq.heappush(heap, (new_height, nr, nc))

        
        # visited = set()
        # rows = len(grid)
        # cols = len(grid[0])
        #
        # @lru_cache(None)
        # def dfs(r, c, maxHeight):
        #     if not(0 <= r < rows and 0 <= c < cols) or (r, c) in visited:
        #         return float('inf')
        #     if r == rows - 1 and c == cols - 1:
        #         return max(maxHeight, grid[r][c])

        #     visited.add((r, c))
        #     dirs = [(1, 0), (-1 , 0), (0, 1), (0, -1)]
            
        #     nextNei = []

        #     for dr, dc in dirs:
        #         nr, nc = r + dr, c + dc
        #         if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
        #             nextNei.append((grid[nr][nc], (nr, nc)))

        #     heapq.heapify(nextNei)
        #     possible_path_maxes = []
        #     while nextNei:
        #         currHeight, (nr, nc) = heapq.heappop(nextNei)

        #         next_path = dfs(nr, nc, max(maxHeight, currHeight))
        #         possible_path_maxes.append(next_path)

        #     visited.remove((r, c))
        #     if possible_path_maxes:
        #         return min(possible_path_maxes)
        #     else:
        #         return float('inf') 

        # return dfs(0, 0, grid[0][0])
