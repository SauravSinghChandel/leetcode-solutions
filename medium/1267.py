class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        rows = [sum(row) for row in grid]
        cols = [sum(grid[i][j] for i in range(n)) for j in range(m)]

        return sum(grid[i][j] and (rows[i] > 1 or cols[j] > 1) for j in range(m) for i in range(n))
