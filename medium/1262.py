class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = sum(nums)

        if res % 3 == 0:
            return res

        r1 = sorted([i for i in nums if i % 3 == 1])
        r2 = sorted([i for i in nums if i % 3 == 2])

        if res % 3 == 1:
            o1 = r1[0] if r1 else float('inf')
            o2 = sum(r2[:2]) if len(r2) > 1 else float('inf')

            return res - min(o1, o2)
        else:
            o1 = r2[0] if r2 else float('inf')
            o2 = sum(r1[:2]) if len(r1) > 1 else float('inf')

            return res - min(o1, o2)
