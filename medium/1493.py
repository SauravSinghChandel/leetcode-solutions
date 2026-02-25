class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = z = res = 0

        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                z += 1
            
            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1


            res = max(r - l, res)

        return res
