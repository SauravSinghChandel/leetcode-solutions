class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        res = 0
        s = 2 * k + 1

        return math.ceil(n / s) * math.ceil(m / s)
