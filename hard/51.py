class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        path = []
        
        cols = set()
        pos = set()
        neg = set()

        def dfs(r):
            if r == n:
                board = []
                for c in path:
                    row = ["."] * n
                    row[c] = 'Q'
                    board.append(''.join(row))

                res.append(board)

            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue

                path.append(c)
                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)

                dfs(r+1)

                path.pop()
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)

        dfs(0)
        return res
        # res = []
        # queens = [i for i in range(n)]
        
        # def isValid(queen):
            
        #     for row in range(len(queen)):
        #         for nextRow in range(row + 1, len(queen)):
        #             if row == 0:
        #                 print(row - queen[row])
        #             if abs(row - nextRow) == abs(queen[row] - queen[nextRow]):
        #                 return False

        #     return True

        # def pathToQueen(path):
        #     q = [['.'] * n for _ in range(n)]
        #     for i in range(len(path)):
        #         idx = path[i]

        #         q[i][idx] = "Q"
        #         q[i] = ''.join(q[i])

        #     return q


        # def dfs(path):
        #     if len(path) == n:
        #         res.append(pathToQueen(path))

        #     for q in queens:
        #         if q in path:
        #             continue
        #         if isValid(path + [q]):
        #             path.append(q)
        #             dfs(path)
        #             path.pop()

        # dfs([])

        # return res
