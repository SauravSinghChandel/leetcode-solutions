class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n
        full = dict() # lake -> last day it rained
        dryDays = []

        for i, v in enumerate(rains):
            if v == 0:
                bisect.insort(dryDays, i)
                res[i] = 1

            else:
                if v in full:
                    idx = bisect.bisect_right(dryDays, full[v])

                    if idx == len(dryDays):
                        return []

                    ddIdx = dryDays.pop(idx)
                    res[ddIdx] = v
                
                full[v] = i

        return res
