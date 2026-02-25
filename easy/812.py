class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(x, y, z):
            return abs(
                x[0] * (z[1] - y[1]) +
                y[0] * (x[1] - z[1]) +
                z[0] * (y[1] - x[1])
            ) / 2

        n = len(points)

        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = points[i], points[j], points[k]
                    res = max(res, area(a, b, c))

        return res
