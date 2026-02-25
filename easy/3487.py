class Solution:
    def maxSum(self, nums: List[int]) -> int:
        posNumSet = set([num for num in nums if num > 0])
        return max(nums) if len(posNumSet) == 0 else sum(posNumSet)
