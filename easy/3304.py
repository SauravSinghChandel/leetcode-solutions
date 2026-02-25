class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        def generateString(word):
            gen = ""
            for c in word:
                gen += chr(((ord(c) - ord('a') + 1) % 25) + ord('a'))

            return word + gen
        
        while len(word) < k:
            word = generateString(word)

        return word[k-1]
