class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"
        nt = len(t)
        ns = len(s)
        res = 0
        resIdx = [-1, -1]
        for i in range(1, nt - 1):
            l = r = i

            while l >= 0 and r < nt and t[l] == t[r]:
                if res < i - l:
                    res  = i - l
                    resIdx = [(l) // 2, (r) // 2]

                l -= 1
                r += 1
        return s[resIdx[0]:resIdx[1]]
