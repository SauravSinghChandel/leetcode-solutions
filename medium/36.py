class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        sqset = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                a = board[r][c]
                sqIdx = (r // 3) * 3 + (c // 3)

                if a in rowset[r] or a in colset[c] or a in sqset[sqIdx]:
                    return False

                rowset[r].add(a)
                colset[c].add(a)
                sqset[sqIdx].add(a)

        return True
