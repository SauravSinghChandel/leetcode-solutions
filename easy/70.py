class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        prev = 2
        prevPrev = 1

        for _ in range(3, n + 1):
            ways = prev + prevPrev

            prevPrev = prev
            prev = ways

        return prev
