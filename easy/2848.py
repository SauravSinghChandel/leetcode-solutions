class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()

        start, end = nums[0]
        n = len(nums)
        res = 0
        for s, e in nums[1:]:
            if s <= end:
                end = max(end, e)
            else:
                res += end - start + 1
                start = s
                end = e
        res += end - start + 1
        return res
