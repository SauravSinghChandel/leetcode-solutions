class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        smallest_row = m
        smallest_col = n

        for op in ops:
            smallest_row = min(smallest_row, op[0])
            smallest_col = min(smallest_col, op[1])
        
        total = smallest_row * smallest_col

        return total
