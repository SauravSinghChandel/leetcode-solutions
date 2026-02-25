class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = min(len(word1), len(word2))
        i = 0
        res = ''
        while i < max_len:
            res += word1[i] + word2[i]
            i += 1
        if len(word1) != len(word2):
            bigger = word1 if len(word2) == max_len else word2
            print("Bigger: ", bigger)
            res += bigger[i:]
        print(res)
        return res
