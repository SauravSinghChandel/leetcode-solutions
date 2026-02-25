class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        unlocked = complexity[0]
        
        mod = 10 ** 9 + 7
        res = 1
        n = len(complexity)
        for i in range(1,n):
            if complexity[i] <= unlocked: return 0
            res = res * i % mod
        return res
