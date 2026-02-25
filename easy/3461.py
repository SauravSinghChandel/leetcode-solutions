class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(c) for c in s]
        while len(s) > 2:
            temp = []
            for i in range(len(s) - 1):
                temp.append((s[i] + s[i + 1]) % 10)
            s = temp
        
        return s[0] == s[1]
