class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        #codes = [''.join(map(str, p)) for p in product([0, 1], repeat = k)]
        
        vals = set()
        for i in range(0, len(s) - k + 1):
            vals.add(s[i:i + k])
        return len(vals) == 2 ** k
