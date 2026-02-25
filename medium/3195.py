class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        INF = float('inf')
        top, left, right, bottom = INF, INF, 0, 0 

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    top = min(top, r)
                    left = min(left, c)
                    right = max(right, c)
                    bottom = max(bottom, r)

        return (right - left + 1) * (bottom - top + 1)
