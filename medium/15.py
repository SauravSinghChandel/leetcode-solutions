class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            
            numbers = nums[n+1:]
            target = 0 - nums[n]
            i = 0
            j = len(numbers) - 1

            while i < j:
                sum = numbers[i] + numbers[j]
                if sum < target:
                    i +=1
                    continue

                elif sum > target:
                    j -=1
                    continue

                elif sum == target:
                    res.append([nums[n], numbers[i], numbers[j]])
                    i += 1
                    while numbers[i] == numbers[i-1] and i < j:
                        i += 1    
                    
        return res
