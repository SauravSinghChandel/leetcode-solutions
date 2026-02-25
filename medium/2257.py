class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        
        for r, c in guards:
            grid[r][c] = 1
 
        
        for r, c in walls:
            grid[r][c] = 2




        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 1 and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3  # Mark as guarded
                    nr += dr
                    nc += dc

        # Count unguarded cells
        return sum(cell == 0 for row in grid for cell in row)
