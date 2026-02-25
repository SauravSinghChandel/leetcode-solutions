class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0

        def strict(arr):
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
        
        for left in range(n):
            for right in range(left, n):

                remaining = nums[:left] + nums[right + 1: ]

                if strict(remaining):
                    count += 1

        return count
