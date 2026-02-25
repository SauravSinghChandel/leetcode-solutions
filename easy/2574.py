class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            left_sum = 0
            right_sum = 0
            # left sum
            if i > 0:
                ldx = 0
                while ldx < i:
                    left_sum += nums[ldx]
                    ldx += 1
            
            if i < len(nums) - 1:
                rdx = i + 1
                while rdx < len(nums):
                    right_sum += nums[rdx]
                    rdx += 1

            res.append(abs(left_sum - right_sum)) 

        return res
