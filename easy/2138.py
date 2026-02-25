class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        n = len(s)
        s = s + fill *  (k - (n % k))
        res = []
        for i in range(0, n, k):
            res.append(s[i:i+k])

        return res
