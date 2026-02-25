class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        def dfs(nums):
            n = len(nums)
            if n == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(n):
                for j in range(n):
                    if i != j:
                        n1 = nums[i]
                        n2 = nums[j]
                        if n2 > n1:
                            n1, n2 = n2, n1

                        rest = [nums[k] for k in range(n) if i != k and j != k]

                        for op in [n1 + n2, n1 - n2, n1 * n2]:

                            if dfs(rest + [op]):
                                return True

                        if n1 > 1e-6 and dfs(rest + [n2 / n1]):
                            return True

                        if n2 > 1e-6 and dfs(rest + [n1 / n2]):
                            return True

            return False

        return dfs(cards)
