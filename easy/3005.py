class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums = Counter(nums).values()
        maxFreq = max(nums)
        return sum(v for v in nums if v == maxFreq)
