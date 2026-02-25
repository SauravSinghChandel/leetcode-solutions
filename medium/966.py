class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set('aeiou')

        def mask(word):
            return "".join(["*" if c in vowels else c for c in word])

        exact = set(wordlist)
        caseIn = {}
        vowelIn = {}

        for word in wordlist:
            lower = word.lower()
            masked = mask(lower)

            caseIn.setdefault(lower, word)
            vowelIn.setdefault(masked, word)

        res = []

        for q in queries:
            ql = q.lower()
            qm = mask(ql)
            if q in wordlist:
                res.append(q)

            elif ql in caseIn:
                res.append(caseIn[ql])

            elif qm in vowelIn:
                res.append(vowelIn[qm])
            else:
                res.append("")
        return res
