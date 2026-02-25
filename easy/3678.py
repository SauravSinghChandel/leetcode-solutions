class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        res = max(math.floor(avg + 1), 1)
        nums = set(nums)
        while res in nums:
            res += 1

        return res
