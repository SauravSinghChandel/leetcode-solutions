class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:

            for i, n in enumerate(row):
                dp[i] = min(dp[i], dp[i + 1]) + n

        return dp[0]
        # n = len(triangle)
        # @lru_cache(None)
        # def dfs(r, c):

        #     if r == n - 1:
        #         return triangle[r][c]

        #     dfs_down = dfs(r + 1, c)
        #     dfs_right = dfs(r + 1, c + 1)

        #     return triangle[r][c] + min(dfs_down, dfs_right)

        # return dfs(0, 0)
