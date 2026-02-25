class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        if len(prices) >= 2:
            r = 1
        profit = prices[r] - prices[l]
        while r != len(prices):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r]-prices[l])

            elif prices[r] < prices[l]:
                l = r

            r += 1

        return max(profit, 0)
