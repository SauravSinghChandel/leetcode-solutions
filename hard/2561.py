class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter = Counter(basket1)

        for k, v in Counter(basket2).items():
            counter[k] -= v

        swaps = []
        minVal = inf
        for k, v in counter.items():
            minVal = min(minVal, k)
            if v == 0:
                continue
            elif v & 1:
                return -1
            else:
                swaps.extend([k] * (abs(v) // 2))

        swaps.sort()
        n = len(swaps) // 2
        res = 0

        for x in swaps[:n]:
            res += min(x, 2 * minVal)

        return res
