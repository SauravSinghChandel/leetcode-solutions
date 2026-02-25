class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def getOps(n):
            power = 1
            res = 0
            ops = 0

            while power <= n:
                r = min(n, power * 4 - 1)
                l = power
                ops += 1

                res +=  (r - l + 1) * ops
                power *= 4

            return res

        return sum((getOps(r) - getOps(l - 1) + 1) // 2 for l, r in queries)
