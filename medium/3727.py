class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(i) for i in nums]
        nums.sort()
        n = len(nums)
        midPoint = n // 2
        total = 0
        for i, v in enumerate(nums):
            if i < midPoint:
                total -= v ** 2
            else:
                total += v ** 2

        return total
