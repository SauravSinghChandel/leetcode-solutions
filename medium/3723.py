class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""

        res = ["0"] * num
        i = 0
        while sum > 0:
            if sum >= 9:
                res[i] = "9"
            else:
                res[i] = str(sum)
            i+= 1
            sum -= 9

        return "".join(res)
