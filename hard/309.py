class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rows = 3
        cols = len(prices)

        dp = [[0] * cols for _ in range(rows)]

        # buy: 0 sell: 1 rest: 2
        dp[0][0] = -prices[0]
        dp[1][0] = float("-inf")

        for c in range(1, cols):
            dp[0][c] = max(dp[0][c - 1], dp[2][c - 1] - prices[c])
            dp[1][c] = dp[0][c - 1] + prices[c]
            dp[2][c] = max(dp[2][c - 1], dp[1][c - 1])

        return max(dp[1][-1], dp[2][-1])
