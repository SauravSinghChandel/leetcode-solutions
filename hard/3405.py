class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        c = math.comb(n - 1, k)

        return (c * m * ((m - 1) ** (n - k - 1)) ) % ((10 ** 9) + 7)
