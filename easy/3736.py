class Solution:
    def minMoves(self, nums: List[int]) -> int:
        t = max(nums)
        return sum(t - i for i in nums)
