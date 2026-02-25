class Solution:
    def sumZero(self, n: int) -> List[int]:
        s = ((n - 1)*(n))/2
        a = -1 * int(s)
        res = [i for i in range(1, n)]
        res.append(a)
        return res
