class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda p: (p[0], -p[1]))
        res = 0
        n = len(points)

        for i in range(n):
            _, yi = points[i]
            maxY = float('-inf')

            for j in range(i + 1, n):
                _, yj = points[j]

                if maxY < yj <= yi:
                    res += 1
                    maxY = yj
        return res
