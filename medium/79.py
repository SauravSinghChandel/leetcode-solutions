class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        rows, cols = len(board), len(board[0])

        def backtrack(row, col, idx):

            if idx == len(word):
                return True

            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visited or board[row][col] != word[idx]:
                return False

            visited.add((row, col))
            res = (
                backtrack(row + 1, col, idx + 1) or
                backtrack(row - 1, col, idx + 1) or
                backtrack(row, col - 1, idx + 1) or
                backtrack(row, col + 1, idx + 1)
            )
            visited.remove((row, col))

            return res

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
