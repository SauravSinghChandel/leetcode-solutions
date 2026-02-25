class Solution:
    def smallestNumber(self, n: int) -> int:
        r = 1
        while True:
            if r >= n:
                return r
            r = r << 1 | 1
        # n = list(str(bin(n)))
        # for i in range(2, len(n)):
        #     if n[i] == "0":
        #         n[i] = '1'

        # return int("".join(n), 2)
