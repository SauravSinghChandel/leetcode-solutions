class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    tile = (row, col)
                    if self.checkRow(tile, mat) and self.checkCol(tile, mat):
                        print(tile)
                        count += 1
        return count

    def checkRow(self, block, mat):
        # Check all the rows
        for i in range(len(mat)):
            if i != block[0]:
                if mat[i][block[1]] == 1:
                    return False
        return True

    def checkCol(self, block, mat):
        for i in range(len(mat[0])):
            if i != block[1]:
                if mat[block[0]][i] == 1:
                    return False
        return True
