class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        def checkCol(matrix, col, num):
            maxNum = float('-inf')
            for r in matrix:
                maxNum = max(maxNum, r[col])

            return num == maxNum

        res = []
        for row in matrix:
            minNum = min(row)
            idx = row.index(minNum)
            if checkCol(matrix, idx, minNum):
                res.append(minNum)

        return res
