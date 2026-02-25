class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        br = set(brokenLetters)
        res = 0
        for w in text.split():
            if any(c in br for c in w):
               continue
            res += 1

        return res
