class Solution:
    def numSteps(self, s: str) -> int:
        res = 0

        carry = 0

        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            curr = bit + carry

            if curr % 2 == 0:
                res += 1

            else:
                res += 2
                carry = 1

        return res
