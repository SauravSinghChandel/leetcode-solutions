class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        path = []

        def dfs(i):
            if sum(path) > target or i == len(candidates):
                return

            path.append(candidates[i])

            if sum(path) == target:
                if path:
                    res.append(path.copy())

            dfs(i)

            path.pop()
            dfs(i+1)

        dfs(0)

        return res
