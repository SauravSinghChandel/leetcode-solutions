class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rmax = [0] * (n + 1)
        cmax = [0] * (n + 1)
        rmin = [n + 1] * (n + 1)
        cmin = [n + 1] * (n + 1)
        
        for x, y in buildings:
            rmin[y] = min(rmin[y], x)
            rmax[y] = max(rmax[y], x)
            cmin[x] = min(cmin[x], y)
            cmax[x] = max(cmax[x], y)

        res = 0

        for x, y in buildings:
            if rmin[y] < x < rmax[y] and cmin[x] < y < cmax[x]:
                res += 1

        return res
