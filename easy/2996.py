class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        val = set(nums)

        for x, y in zip(nums, nums[1:]):
            if x + 1 == y:
                total += y
            else:
                break
        
        while total in val:
            total += 1

        return total
