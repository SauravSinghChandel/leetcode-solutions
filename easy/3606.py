class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        bSet = {"electronics", "grocery", "pharmacy", "restaurant"}
        e, g, p, r = [], [], [], []
        for c, b, a in zip(code,businessLine, isActive):
            if not a:
                continue
            
            if b not in bSet:
                continue

            if not c or not all(ch.isalnum() or ch == "_" for ch in c):
                continue

            if b[0] == 'e': e.append(c)
            if b[0] == 'g': g.append(c)
            if b[0] == 'p': p.append(c)
            if b[0] == 'r': r.append(c)

        return sorted(e) + sorted(g) + sorted(p) + sorted(r)
