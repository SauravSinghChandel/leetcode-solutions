class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxVal = max(nums)
        bits = 0 if maxVal == 0 else 1 + math.floor(math.log2(maxVal))

        nearest_setbit = [n] * bits
        res = [0] * n

        for i in range(n - 1, -1, -1):
            nearest = i

            for j in range(bits):
                if nums[i] & (1 << j):
                    nearest_setbit[j] = i

                elif nearest_setbit[j] != n:
                    nearest = max(nearest, nearest_setbit[j])

            res[i] = nearest - i + 1

        return res
