class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total = sum(nums[:k])
        res = total / k

        n = len(nums)

        for i in range(k, n):
            total += nums[i] - nums[i - k]

            res = max(res, total / k)
        return res
