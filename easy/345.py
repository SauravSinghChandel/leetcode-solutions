class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list("AEIOUaeiou")

        vowelsInWord = []

        for i in s:
            if i in vowels:
                vowelsInWord.append(i)
        
        vowelsInWord.reverse()

        counter = 0
        res = ''
        for i in s:
            if i in vowels:
                res += vowelsInWord[counter]
                counter += 1
            else:
                res += i

        return res
