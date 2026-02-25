class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        sqset = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    
                    curr = board[r][c]
                    sqIdx = (r // 3) * 3 + (c // 3)

                    rowset[r].add(curr)
                    colset[c].add(curr)
                    sqset[sqIdx].add(curr)

        n = len(empties)
        def backtrack(i = 0):
            if i == n:
                return True

            r, c = empties[i]
            sqIdx = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if num not in rowset[r] and num not in colset[c] and num not in sqset[sqIdx]:
                    board[r][c] = num
                    rowset[r].add(num)
                    colset[c].add(num)
                    sqset[sqIdx].add(num)

                    if backtrack(i + 1):
                        return True
                    
                    board[r][c] = "."
                    rowset[r].remove(num)
                    colset[c].remove(num)
                    sqset[sqIdx].remove(num)

            return False

        backtrack()
