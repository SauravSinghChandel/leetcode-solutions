class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and (n - 1) % 3 == 0
        # if n <= 0:
        #     return False
        # n = math.log(n, 4)
        # return n == int(n)
