class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(sub, diff, n):
            if n == 0 and diff == 0:
                res.append(sub)

            if diff >= 1:
                dfs(sub + ")", diff - 1, n)

            if n >= 1:
                dfs(sub + "(", diff + 1, n - 1)

        dfs("", 0, n)
        return res
        # res = []

        # def dfs(sub, closeCount, openCount):

        #     if len(sub) == 2 * n:
        #         res.append(sub)
            
        #     if openCount < n:
        #         dfs(sub + "(", closeCount, openCount + 1)

        #     if closeCount < openCount:
        #         dfs(sub + ")", closeCount + 1, openCount)

        # dfs("", 0, 0)

        # return res
