class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        prev = -1000000000
        res = 0

        for n in nums:
            curr = min(max(n - k, prev + 1), n + k)

            if curr > prev:
                res += 1
                prev = curr

        return res
