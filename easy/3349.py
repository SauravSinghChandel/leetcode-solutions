class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        pre, curr = 0, 1
        if k == 1:
            return True
        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]: curr += 1
            else:
                pre = curr
                curr = 1

            if curr >= k and pre >= k or curr // 2 >= k: return True

        return False
