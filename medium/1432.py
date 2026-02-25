class Solution:
    def maxDiff(self, num: int) -> int:
        a = str(num)
        b = str(num)

        if len(a) == 1:
            return 8

        for c in a:
            if c != '9':
                a = a.replace(c, '9')
                break

        if b[0] != '1':
            b = b.replace(b[0], '1')
        
        else:
            for c in b[1:]:
                if c not in {'0', '1'}:
                    b = b.replace(c, '0')
                    break

        return int(a) - int(b)
