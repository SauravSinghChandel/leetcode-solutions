class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        preSum = [float('inf')] * k
        pre = 0
        res = float('-inf')
        preSum[0] = 0

        for i, n in enumerate(nums):
            pre += n
            mod = (i + 1) % k
            res = max(res, pre - preSum[mod])
            preSum[mod] = min(pre, preSum[mod])

        return res







        ps = [float('inf')] * k
        ps[0] = 0
        pre = 0
        res = float('-inf')

        for i, n in enumerate(nums):
            pre += n
            mod = (i + 1) % k

            res = max(res, pre - ps[mod])
            ps[mod] = min(pre, ps[mod])

        return res
