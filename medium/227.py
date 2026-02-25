class Solution:
    def calculate(self, s: str) -> int:
        s = list(s)
        res = []

        n = len(s)
        num = 0
        sign = "+"
        op = {"+", "-", "/", "*"}
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in op or i == n - 1:
                if sign == "+":
                    res.append(num)
                elif sign == '-':
                    res.append(-num)
                elif sign == "*":
                    prev = res.pop()
                    res.append(prev * num)
                elif sign == "/":
                    prev = res.pop()
                    res.append(int(prev / num))

                sign = ch
                num = 0

        return sum(res)
