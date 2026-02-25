class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # stack = {height, idx, prevCount}
        # Check if top of stack is smaller than val in histogram
        # Calculate count of the idx, gap * height + prevCount
        # Push to the stack
        # Update histogram for next row
        res = 0
        rows, cols = len(mat), len(mat[0])
        his = [0] * cols

        for r in range(rows):
            for j in range(cols):
                his[j] = his[j] + 1 if mat[r][j] == 1 else 0

            s = [(-1, -1, 0)]
            for c in range(cols):

                while s[-1][0] >= his[c]:
                    s.pop()

                prevH, prevI, prevC = s[-1]
                gap = c - prevI
                height = his[c]

                count = gap * height + prevC
                s.append((height, c, count))
                res += count
            
        return res
