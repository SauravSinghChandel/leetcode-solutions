class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        def dfs(i, path):

            if len(path) > 1:
                res.add(tuple(path))
            
            if i == n:
                return

            for j in range(i, n):
                if not path or nums[j] >= path[-1]:
                    dfs(j + 1, path + [nums[j]])
        dfs(0, [])
        return list(res)
