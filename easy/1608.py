
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # nums.sort()
        # prev = -1

        # counter = len(nums)

        # for i in range(len(nums)):
        #     if prev == nums[i]:
        #         counter -= 1
        #         prev = nums[i]
        #         continue

        #     if nums[i] == counter:
        #         return counter
            
        #     if prev < counter < nums[i]:
        #         return counter

        #     counter -= 1
        #     prev = nums[i]
        
        # return -1

        count = [0] * (len(nums) + 1)
        for n in nums:
            index = min(n, len(nums))

            count[index] += 1

        total_right = 0

        for i in reversed(range(len(nums) + 1)):
            total_right += count[i]

            if i == total_right:
                return i

        return -1
