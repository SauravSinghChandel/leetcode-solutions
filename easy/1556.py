class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ""
        n = str(n)
        m = len(n)
        if m < 4:
            return n
        for i in range(-1, -m - 1, -1):
            res = n[i] + res
            if -i % 3 == 0:
                res = "." + res


        if res[0] == ".":
            return res[1:]
        return res
