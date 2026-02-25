class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        best, res = s, 0
        for k in range(n):
            first, last = s[:k], s[k:]
            first, last = first[::-1] + last, first + last[::-1]

            if first < best or last < best:
                best = min(first, last)

        return best
