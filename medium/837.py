class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # prob of <= n points
        # stops at k or more points
        # [1, maxPts] draw range
        # if k < n and n - k + 1 >= maxPts : return 1
        # if k < n  and n - k + 1< maxPts: return (n - k + 1) / maxPTs

        windowSum = n - k + 1

        if windowSum >= maxPts or k == 0:
            return 1

        dp = [0] *  (n + 1)

        for i in range(k, n + 1):
            dp[i] = 1


        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            windowSum += dp[i]
            if i + maxPts <= n:
                windowSum -= dp[i + maxPts]

        return dp[0]
