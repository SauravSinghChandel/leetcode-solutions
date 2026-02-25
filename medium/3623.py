class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        lines = defaultdict(int)

        for px, py in points:
            lines[py] += 1

        sum_a = 0
        sum_a2 = 0

        for v in lines.values():
            if v > 1:
                a = (v * (v - 1)) // 2
                sum_a += a
                sum_a2 += a ** 2
        
        res = (sum_a ** 2 - sum_a2) // 2
        return res % mod
