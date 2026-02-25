class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        Max, Min = max(nums), min(nums)

        for i in nums:
            if i != Max and i != Min:
                return i

        return -1
