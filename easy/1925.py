class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n):
            for j in range(1, n):
                c = sqrt(i ** 2 + j ** 2)
                if c <= n and int(c) == c:
                    res += 1
        
        return res
