class Solution:
    def maxOperations(self, s: str) -> int:
        cnt = 0
        res = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "0":
                while i + 1 < n and s[i + 1] == "0":
                    i += 1
                
                res += cnt

            else:
                cnt += 1
            i += 1
        
        return res
