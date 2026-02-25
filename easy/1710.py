class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : (-x[1], x[0]))
        count = 0
        res = 0
        for box, units in boxTypes:
            if box + count > truckSize:
                res += (truckSize - count) * units
                return res

            res += box * units
            count += box

        return res
