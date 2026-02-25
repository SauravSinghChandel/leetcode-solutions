class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffs = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        

        diffs.sort(reverse=True)

        base = sum(reward2)

        return base + sum(diffs[:k])
