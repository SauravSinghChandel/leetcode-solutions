class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = "".join([str(ord(i) - 96) for i in s])

        for _ in range(k):
            res = str(sum([int(i) for i in res]))

        return int(res)
