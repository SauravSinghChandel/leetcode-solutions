class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        xstr, ystr = 'ab', 'ba'
        if y > x:
            x, y = y, x
            xstr, ystr = ystr, xstr

        res = 0
        xs, ys = [], []
        for c in s:
            
            if xs and c == xstr[1] and xs[-1] == xstr[0]:
                xs.pop()
                res += x
            else:
                xs.append(c)
        print(xs)
        for c in xs:
            if ys and c == ystr[1] and ys[-1] == ystr[0]:
            
                ys.pop()
                res += y
            else:
                ys.append(c)

        return res
