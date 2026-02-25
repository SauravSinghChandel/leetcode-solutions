class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @lru_cache(None)
        def dfs(i, j):

            if j - i < 2:
                return 0
            
            res = float('inf')
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + (values[i] * values[j] * values[k]))

            return res
        return dfs(0, n - 1)
