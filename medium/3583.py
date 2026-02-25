class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        res = 0
        left = Counter()
        right = Counter(nums)

        for x in nums:

            right[x] -= 1

            t = 2 * x

            res += (left[t] * right[t]) % mod

            left[x] += 1

        return res % mod
