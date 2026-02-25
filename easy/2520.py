class Solution:
    def countDigits(self, num: int) -> int:
        dig = dict()
        res = 0

        for i, c in enumerate(str(num)):
            if c in dig:
                if dig[c]:
                    res += 1

            else:
                if num % int(c) == 0:
                    res += 1
                    dig[c] = True
                else:
                    dig[c] = False

        return res
