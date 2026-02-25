class Solution:
    def binaryGap(self, n: int) -> int:
        b = str(bin(n))[2:]
        bl = len(b)
        l = 0
        while b[l] != '1':
            l += 1
            if l == bl - 1:
                return 0
        res = 0
        for r in range(l + 1, bl):
            if b[r] == "1":
                res = max(res, r - l)
                l = r
        return res
