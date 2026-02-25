class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = set("AIEOUaieou")
        hasV, hasC = False, False
        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in vowels:
                    hasV = True
                else: 
                    hasC = True

        return hasV and hasC
