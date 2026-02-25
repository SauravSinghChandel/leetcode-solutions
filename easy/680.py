class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        deleted = False
        resL = resR = ""
        def check(string):
            return string == string[::-1]

        if check(s):
            return True
        
        else:
            while l <= r:
                if s[l] != s[r]:
                    return check(s[l+1:r+1]) or check(s[l:r])
                l += 1
                r -= 1
