class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        table = []
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            val = i ** x
            if val <= n:
                table.append(val)
            else:
                break
        dp = [0] * (n + 1)
        dp[0] = 1
        for power in table:
            for target in range(n, power - 1, -1):
                dp[target] = (dp[target] + dp[target - power]) % mod
            
        return dp[n]
