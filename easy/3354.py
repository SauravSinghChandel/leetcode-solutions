class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        win = 0
        tot = sum(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                if 2 * win == tot:
                    res += 2

                if abs((2 * win) - tot) == 1:
                    res += 1

            win +=  nums[i]

        return res
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         lsum = sum(nums[:i])
        #         rsum = sum(nums[i:])

        #         if lsum == rsum:
        #             res += 2
                
        #         if abs(lsum - rsum) == 1:
        #             res += 1
        # return res
