class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * n for _ in range(n)]
        diags = defaultdict(list)

        for r in range(n):
            for c in range(n):
                diags[r - c].append(grid[r][c])

        for k, v in diags.items():
            if k < 0: # Top right
                v.sort(reverse=True)
            else:
                v.sort()

        for r in range(n):
            for c in range(n):
                res[r][c] = diags[r - c].pop()

        return res
