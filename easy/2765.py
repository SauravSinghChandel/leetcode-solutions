class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        seq = -1
        res = -1
        n = len(nums)
        for i in range(1, n):
            if seq > 0 and nums[i] == nums[i - 2]:
                seq += 1
            elif nums[i] == nums[i - 1] + 1:
                seq = 2
            else:
                seq = -1
            res = max(res, seq)
        return res
        # max_len = -1
        # n = len(nums)

        # for start in range(n - 1):
        #     if nums[start + 1] - nums[start] != 1:
        #         continue
        #     length = 2
        #     for i in range(start + 2, n):
        #         expected = nums[start] if (i - start) % 2 == 0 else  nums[start + 1]

        #         if nums[i] == expected:
        #             length += 1
        #         else:
        #             break
        #     max_len = max(max_len, length)

        # return max_len
