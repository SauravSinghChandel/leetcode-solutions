class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1

        dp = [[0] * cols for _ in range(rows)]

        res = ""

        for r in range(rows - 2, -1, -1):
            for c in range(cols -2, -1, -1):

                if text1[r] == text2[c]:
                    dp[r][c] = dp[r + 1][c + 1] + 1

                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        r = c = 0
        text1 += " "
        text2 += " "
        while r < rows - 1 and c < cols - 1:
            # print(f"R: {r}, C: {c}")
            if text1[r] == text2[c]:
                res += text1[r]
                r += 1
                c += 1
            else:
                if dp[r + 1][c] > dp[r][c + 1]:
                    r += 1
                elif dp[r + 1][c] < dp[r][c + 1]:
                    c += 1
                else:
                    r += 1
                    c += 1

        print(res)
        print(" ", end = "")
        for c in text2:
            print(" ", c, end = "")
        print()
        for i, row in enumerate(dp):
            print(text1[i], row)

        return dp[0][0]
