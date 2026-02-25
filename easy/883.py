class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        col_max = [0] * cols

        for r in range(rows):
            # XZ - plane
            res += max(grid[r])
            for c in range(cols):
                # XY - plane
                if grid[r][c] > 0:
                    res += 1
                col_max[c] = max(col_max[c], grid[r][c])

        res += sum(col_max)

        return res
