class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1

            else:
                res += ((count) * (count + 1)) / 2
                count = 0
        res += ((count) * (count + 1)) / 2
        return int(res)
