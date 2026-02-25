class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        vowChars = [c for c in s if c in vowels]

        vowChars.sort()

        res = []
        vIdx = 0
        for c in s:
            if c in vowels:
                res.append(vowChars[vIdx])
                vIdx += 1
            else:
                res.append(c)

        return ''.join(res)
        # cosIdx = []
        # cos = []
        # vow = []
        # vowIdx = []
        # vowels = {'a', 'e', 'i', 'o', 'u'}
        # n = len(s)

        # for i in range(n):
        #     if s[i].lower() in vowels:
        #         vow.append(s[i])
        #         vowIdx.append(i)
        #     else:
        #         cos.append(s[i])
        #         cosIdx.append(i)

        # vow.sort()

        # res = [0] * n

        # for i in range(len(vow)):
        #     res[vowIdx[i]] = vow[i]

        # for i in range(len(cos)):
        #     res[cosIdx[i]] = cos[i]

        # return ''.join(res)
