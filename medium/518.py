class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        rows = len(coins) + 1
        cols = amount + 1

        dp = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            dp[r][0] = 1
            
        for i in range(1, rows):
            for j in range(1, cols):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]
