class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        num = 0

        for n in nums:
            num = (num * 2 + n) % 5
            res.append(num % 5 == 0)
        return res
        # num = ''

        # for n in nums:
        #     num += str(n)
        #     res.append(int(num, 2) % 5 == 0)

        # return res
