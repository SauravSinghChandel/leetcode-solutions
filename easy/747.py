class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        f, s = -1, -1
        for n in nums:
            if n > f:
                s, f = f, n


            if n < f:
                s = max(s, n)
        if f >= 2 * s:
            return nums.index(f)
        return -1
