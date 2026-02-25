class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
        # og = original
        # nums.sort()
        # n = len(nums)

        # for i in range(n):
        #     if nums[i] == og:
        #         og *= 2
            
        # return og
