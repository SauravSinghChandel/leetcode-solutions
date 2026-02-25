class Solution(object):
    def isPalindrome(self, s):
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 += i.lower()
        if s1 == s1[::-1]:
            return True
