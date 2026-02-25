class Solution:
    def numSub(self, s: str) -> int:
        mod = 10 ** 9 + 7

        res = 0
        curr = 0

        for c in s:
            if c == "1":
                curr += 1
                res += curr

            else:
                curr = 0

        return res % mod
