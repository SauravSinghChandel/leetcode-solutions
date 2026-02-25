from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        next_value = {1: 2, 2: 0, 0: 2}  # cycle mapping
        diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]  # four diagonals

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        @cache
        def dfs(r: int, c: int, dr: int, dc: int, turned: bool) -> int:
            l = 1
            expected = next_value[grid[r][c]]

            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and grid[nr][nc] == expected:
                l = 1 + dfs(nr, nc, dr, dc, turned)

            if not turned:
                turnr, turnc = dc, -dr
                tr, tc = r + turnr, c + turnc
                if is_valid(tr, tc) and grid[tr][tc] == expected:
                    l = max(l, 1 + dfs(tr, tc, turnr, turnc, True))

            return l

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr, dc in diagonals:
                        res = max(res, dfs(r, c, dr, dc, False))

        return res
