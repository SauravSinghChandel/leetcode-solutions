class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)

        dp[1] = 1
        prefix[1] = 1

        for i in range(2, n + 1):
            l = max(0, i - forget)
            r = i - delay
            if r >= 0:
                dp[i] = (prefix[r] - prefix[l]) % MOD
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD

        ans = sum(dp[max(1, n - forget + 1): n + 1]) % MOD
        return ans
