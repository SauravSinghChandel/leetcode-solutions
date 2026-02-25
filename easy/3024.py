class Solution:
    def triangleType(self, nums: List[int]) -> str:
        count = 0
        for i in range(len(nums)):
            if nums[i] >= nums[i-1] + nums[i-2]:
                return "none"
            
            if i + 1 < len(nums):
                for j in range(i + 1, len(nums)):
                    if nums[i] == nums[j]:
                        count += 1
        
        if count == 3:
            return 'equilateral'
        if count == 1:
            return 'isosceles'
        if count == 0:
            return 'scalene'
