class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        visited = set()
        if k % 2 == 0 or k % 5 == 0:
            return -1
        res = 0
        for l in range(1, k + 1):
            res = (res * 10 + 1) % k
            if res == 0:
                return l
        return -1
