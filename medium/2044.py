class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = 0
        maxOR = 0

        for x in nums:
            maxOR |= x
        n = len(nums)
        def dfs(i, currOR):
            nonlocal res
            if i == n:
                if currOR == maxOR:
                    res += 1
                return

            dfs(i + 1, currOR | nums[i])
            dfs(i + 1, currOR)

        dfs(0, 0)
        return res
