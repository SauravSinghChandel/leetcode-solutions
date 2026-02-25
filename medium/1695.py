class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        total = nums[0]
        l = 0
        res = total
        n = len(nums)
        seen = set()
        seen.add(nums[0])
        for r in range(1, n):
            if nums[r] in seen:
                res = max(res, total)
                total -= nums[l]
                seen.remove(nums[l])
                l += 1
                while l < r and nums[r] in seen:
                    total -= nums[l]
                    seen.remove(nums[l])
                    l += 1
                
            total += nums[r]
            seen.add(nums[r])
            res = max(total, res)
        return res
