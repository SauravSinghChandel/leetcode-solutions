class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pV = set()
        aV = set()

        def dfs(r, c, visited, pH):

            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or heights[r][c] < pH:
                return
            
            dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])

        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, pV, 0)
                
                if r == rows - 1 or c == cols - 1:
                    dfs(r, c, aV, 0)

        return list(pV & aV)




















        # rows, cols = len(heights), len(heights[0])
        # pacific, atlantic = set(), set()
        # res = []

        # def dfs(r, c, visited, prevHeight):
        #     if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < prevHeight:
        #         return

        #     visited.add((r, c))

        #     for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #         dfs(r + dr, c + dc, visited, heights[r][c])

        # # For Top and Bottom
        # for c in range(cols):
        #     dfs(0, c, pacific, heights[0][c])
        #     dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # # For Left and Right
        # for r in range(rows):
        #     dfs(r, 0, pacific, heights[r][0])
        #     dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # return list(pacific & atlantic)
