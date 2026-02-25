class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex + 1):
            res.append(comb(rowIndex, i))

        return res
