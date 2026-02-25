class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        prevC = word[0]
        count = 1
        for i in range(1, len(word)):
            c = word[i]

            if c == prevC and count < 9:
                count += 1
                continue

            elif count == 9:
                comp += '9' + prevC
                count = 1
            else:
                comp += str(count) + prevC
                count = 1
            
            prevC = c
        comp += str(count) + prevC
        return comp
