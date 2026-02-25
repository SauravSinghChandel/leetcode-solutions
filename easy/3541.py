class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        vD, cD = defaultdict(int), defaultdict(int)
        if s == "":
            return 0
        for c in s:
            if c in vowels:
                vD[c] += 1
            else:
                cD[c] += 1
        
        if not vD.values():
            return max(cD.values())
        if not cD.values():
            return max(vD.values())

        return max(vD.values()) + max(cD.values())
