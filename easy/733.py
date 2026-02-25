class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image

        def dfs(r, c):

            if not (0 <= r < len(image)) or not (0 <= c < len(image[0])):
                return

            if image[r][c] != original_color:
                return

            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)

        return image
























        # adjacent = [[-1, 0],
        #             [0, -1],
        #             [1, 0],
        #             [0, 1]]

        # original_color = image[sr][sc]

        # stack = [(sr, sc)]
        # visited = set()

        # while stack:
        #     curr = stack.pop()
        #     print(curr)
        #     if image[curr[0]][curr[1]] == original_color:
        #         image[curr[0]][curr[1]] = color
        
        #         for dx, dy in adjacent:
        #             new_dx = (curr[0] + dx)
        #             new_dy = (curr[1] + dy)
                    
        #             if (new_dx, new_dy) not in visited and (0 <= new_dx < len(image)) and (0 <= new_dy < len(image[0])):

        #                 stack.append((new_dx, new_dy))
        #                 visited.add((new_dx, new_dy))
        # return image
