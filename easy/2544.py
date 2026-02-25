class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        total = 0
        for (i, j) in enumerate (n):
            total += ((-1)**i) * int(j)

        return total
