class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.00000
        def backtrack(a, b, memo = {}):

            if (a, b) in memo:
                return memo[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5
            
            if a <= 0:
                return 1

            if b <= 0:
                return 0

            firstOperation = 0.25 * backtrack(a - 100, b, memo)
            secondOperation = 0.25 * backtrack(a - 75, b - 25, memo)
            thirdOperation = 0.25 * backtrack(a - 50, b - 50, memo)
            fourthOperation = 0.25 * backtrack(a - 25, b - 75, memo)

            memo[(a, b)] = firstOperation + secondOperation + thirdOperation + fourthOperation

            return memo[(a, b)]

        return backtrack(n, n)
