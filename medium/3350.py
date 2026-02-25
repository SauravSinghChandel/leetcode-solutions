class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0
        curr = 1
        start = 0
        res = 0
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                curr = i - start
                start = i
                res = max(res, curr // 2, min(prev, curr))
                prev = curr
        curr = n - start
        return max(res, curr // 2, min(prev, curr))

        # n = len(nums)
        # if n <= 1:
        #     return 0
        # if n == 2:
        #     return 1
        # runs = []
        # l = 1
        # for i in range(1, n):
        #     if nums[i] > nums[i - 1]:
        #         l += 1            
        #     else:
        #         runs.append(l)
        #         l = 1
        # runs.append(l)
        # k = 0
        # maxLen = runs[0]
        # for i in range(1, len(runs)):
        #     k = max(k, min(runs[i], runs[i - 1]))
        #     maxLen = max(runs[i], maxLen)        
        # return max(k, maxLen // 2)
