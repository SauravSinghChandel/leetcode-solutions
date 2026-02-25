class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0

        for n in nums:
            curr = n % k

            for prev in range(k):
                dp[curr][prev] = dp[prev][curr] + 1
                res = max(dp[curr][prev], res)

        return res
