class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        minVal = nums[0]
        res = -1
        for R in range(len(nums)):
            if nums[R] > minVal:
                res = max(res, nums[R] - minVal)

            else:
                minVal = nums[R]

        return res if res >= 0 else -1
