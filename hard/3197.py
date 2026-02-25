class Solution:
    def findBoundingBox(self, grid):
        INF = float('inf')
        top, left, right, bottom = INF, INF, 0, 0 

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    top = min(top, r)
                    left = min(left, c)
                    right = max(right, c)
                    bottom = max(bottom, r)

        return top, bottom, left, right

    def minArea(self, x1, x2, y1, y2, grid):
        INF = float('inf')
        min_x, max_x = INF, -1
        min_y, max_y = INF, -1

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if grid[i][j] == 1:
                    min_x = min(i, min_x)
                    max_x = max(i, max_x)
                    min_y = min(j, min_y)
                    max_y = max(j, max_y)

        if min_x == INF or min_y == INF or max_y == -1 or max_x == -1:
            return INF

        return (max_x - min_x + 1) * (max_y - min_y + 1)

    def minimumSum(self, grid: List[List[int]]) -> int:
        INF = float('inf')
        top, bottom, left, right = self.findBoundingBox(grid)

        res = INF

        for i in range(top, bottom):
            for j in range(left, right):

                for case in range(4):
                    if case == 0: #Up
                        area = (self.minArea(top, i, left, j, grid) + 
                                self.minArea(top, i, j + 1, right, grid) +
                                self.minArea(i + 1, bottom, left, right, grid))

                    if case == 1: #Right
                        area = (self.minArea(top, bottom, left, j, grid) +
                                self.minArea(top, i, j + 1, right, grid) + 
                                self.minArea(i + 1, bottom, j + 1, right, grid))

                    if case == 2: #Down
                        area = (self.minArea(top, i, left, right, grid) +
                                self.minArea(i + 1, bottom, left, j, grid) +
                                self.minArea(i + 1, bottom, j + 1, right, grid))
                    if case == 3: #Left
                        area = (self.minArea(top, i, left, j, grid) +
                                self.minArea(i + 1, bottom, left, j, grid) +
                                self.minArea(top, bottom, j + 1, right, grid))

                    res = min(area, res)
        
        # Horizontal Slicing
        for i in range(top, bottom - 1):
            for j in range(i + 1, bottom):
                area = (self.minArea(top, i, left, right, grid) +
                        self.minArea(i + 1, j, left, right, grid) +
                        self.minArea(j + 1, bottom, left, right, grid))
                
                res = min(area, res)

        for i in range(left, right - 1):
            for j in range(i + 1, right):
                area = (self.minArea(top, bottom, left, i, grid) +
                        self.minArea(top, bottom, i + 1, j, grid) +
                        self.minArea(top, bottom, j + 1, right, grid))

                res = min(area, res)

        return res
