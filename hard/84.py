#__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Check for right extension
        # Keep pushing to stack while increasing
        # If decreasing, keep popping until less than equal to
        # can be extended to left as well
        # Finish popping the stack as long as possible

        n = len(heights)
        res = -1
        stack = [] # (idx, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()

                res = max(res, ((i - idx) * height))
                start = idx

            stack.append((start, h))

        for i, h in stack:
            res = max(res, (n - i) * h)

        return res
