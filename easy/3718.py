class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        multiples = [i * k for i in range(1, 102)]
        nums = set(nums)
        for m in multiples:
            if m not in nums:
                return m
