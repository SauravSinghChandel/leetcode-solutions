class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        curr = 1
        n = len(prices)

        for i in range(n):
            if i > 0 and prices[i] - prices[i - 1] == -1:
                curr += 1
            else:
                curr = 1

            res += curr

        return res
