class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # res = 0
        # for i in range(1, n + 1):

        #     if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        #         res += i

        # return res
        def helper(n):
            return (n * (n + 1))/2

        return int(
            helper(n//3) * 3 + helper(n//5) * 5 + helper(n//7) * 7
            - helper(n//15) * 15 - helper(n//21) * 21 - helper(n//35) * 35
            + helper(n//105) * 105
        )
