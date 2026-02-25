class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        n = len(nums)

        res = 0

        for i in range(n-1):
            l += nums[i]
            r -= nums[i]
            if abs(l - r) % 2 == 0:
                res += 1

        return res
