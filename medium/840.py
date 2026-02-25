class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        checkSet = set(range(1, 10))
        def isMagic(r, c):
            nonlocal checkSet
            if grid[r][c] != 5:
                return False

            vals = [grid[i][j] for i in range(r - 1, r + 2) for j in range(c - 1, c + 2)]

            if set(vals) != checkSet:
                return False

            s = grid[r - 1][c] + grid[r][c] + grid[r + 1][c]

            if grid[r - 1][c - 1] + grid[r][c - 1] + grid[r + 1][c - 1] != s: return False
            if grid[r - 1][c + 1] + grid[r][c + 1] + grid[r + 1][c + 1] != s: return False

            if grid[r - 1][c - 1] + grid[r - 1][c] + grid[r - 1][c + 1] != s: return False
            if grid[r + 1][c - 1] + grid[r + 1][c] + grid[r + 1][c + 1] != s: return False
            if grid[r][c - 1] + grid[r][c] + grid[r][c + 1] != s: return False

            if grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1] != s: return False
            if grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1] != s: return False
            
            return True


        res = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if isMagic(r, c):
                    res += 1

        return res
