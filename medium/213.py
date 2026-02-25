class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxSum(houses):
            prev = curr = 0

            if len(nums) == 1:
                return nums[0]
            
            for h in houses:
                prev, curr = curr, max(curr, prev + h)

            return curr

        return max(maxSum(nums[1:]), maxSum(nums[:len(nums) - 1]))
