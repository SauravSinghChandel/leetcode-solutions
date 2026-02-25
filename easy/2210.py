class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0

        n = len(nums)
        i = 1

        left = nums[i - 1]
        curr = nums[i]
        right = nums[i + 1]
        while i < n - 1:
            while curr == right and i < n - 2:
                i += 1
                curr = nums[i]
                right = nums[i + 1]

            if left > curr and right > curr:
                res += 1
            elif (left < curr and right < curr):
                res += 1
            
            i += 1
            left = nums[i - 1]
            curr = nums[i]
            if i < n - 1:
                right = nums[i + 1]
            else:
                return res
        return res
