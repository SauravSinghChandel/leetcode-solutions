class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(mat), len(mat[0])
        x = rows + cols - 1

        for d in range(x):
            idxs = []

            for r in range(max(0, d - cols + 1), min(rows, d + 1)):
                c = d - r
                if c < cols:
                    idxs.append((r, c))
                
            if d % 2 == 0:
                idxs.reverse()

            res += [mat[r][c] for r, c in idxs]
        return res
