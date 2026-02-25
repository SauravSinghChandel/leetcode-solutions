class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []

        potions.sort()
        pn = len(potions)

        for s in spells:
            s = success / s
            l = bisect.bisect_left(potions, s)
            res.append(pn - l)

        return res
