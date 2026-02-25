class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        INF = float('inf')
        n = len(fruits)
        res = sum([fruits[i][i] for i in range(n)])

        def make_dfs(dirs):
            @lru_cache(None)
            def dfs(r, c, moves):

                if r == n - 1 and c == n - 1:
                    return 0 if moves == 0 else INF

                if moves == 0 or r == c:
                    return INF

                best = -1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        val = dfs(nr, nc, moves - 1)

                        if val != INF:
                            best = max(val, best)

                return INF if best < 0 else fruits[r][c] + best

            return dfs

        lower = [(1, -1), (1, 0), (1, 1)]
        upper = [[-1, 1], [0, 1], [1, 1]]

        dfs_lower = make_dfs(lower)
        res += dfs_lower(0, n - 1, n - 1)

        dfs_upper = make_dfs(upper)
        res += dfs_upper(n - 1, 0, n - 1)

        return res
