class Solution:
    def arrangeCoins(self, n: int) -> int:

        for i in range(2**17 + 10):
            summy = (i*(i+1))/2

            if summy == n:
                return i

            if summy > n:
                return i - 1
