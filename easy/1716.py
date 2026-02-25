class Solution:
    def totalMoney(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        res = 1
        for i in range(1, n):
            if i % 7 == 0:
                dp[i] = dp[i - 7] + 1
            else:
                dp[i] = dp[i - 1] + 1

            res += dp[i]

        return res
