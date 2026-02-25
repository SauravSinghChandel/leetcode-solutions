class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        res = [i for i in range(left, right + 1)]
        megaSet = set()

        for l, r in ranges:
            for i in range(l, r + 1):
                megaSet.add(i)

        for i in res:
            if i not in megaSet:
                return False

        return True
