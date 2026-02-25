class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        soldier_count = sorted([(i, sum(row)) for i, row in enumerate(mat)], key=lambda x: (x[1], x[0]))
        print(soldier_count)
        for i in range(k):
            res.append(soldier_count[i][0])

        return res
