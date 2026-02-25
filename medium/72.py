class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1) + 1
        cols = len(word2) + 1

        dp = [[0] * cols for _ in range(rows)]

        for r in range(1, rows):
            dp[r][0] = r

        for c in range(1, cols):
            dp[0][c] = c

        for r in range(1, rows):
            for c in range(1, cols):

                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                
                else:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1

        r = c = 0
        text1 = word1 + " "
        text2 = word2 + " "
        res = ""
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

        print("Answer: ", res)
        print("\n")
        print(" ", end = "")
        for c in text2:
            print(" ", c, end = "")
        print()
        for i, row in enumerate(dp):
            print(text1[i], row)

        return dp[rows - 1][cols - 1]
