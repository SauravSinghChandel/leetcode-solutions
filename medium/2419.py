class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        count = 0
        maxVal = max(nums)

        for num in nums:
            if num == maxVal:
                count += 1
                res = max(count, res)

            else:
                count = 0

        return res
